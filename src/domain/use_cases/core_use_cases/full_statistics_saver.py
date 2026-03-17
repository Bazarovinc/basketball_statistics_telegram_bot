import asyncio
from io import BytesIO
from typing import TYPE_CHECKING

from loguru import logger
from pydantic_core._pydantic_core import ValidationError

from src.constants import PROFILES_PATH, TEAMS_PATH
from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.core.exceptions.parsers_exceptions import URLValidationException
from src.core.exceptions.repo_exceptions import DuplicatedRecordException
from src.core.exceptions.use_case_exceptions import (
    PlayerProfileAlreadySavedError,
    UserAgreementNotFoundError,
    UserNotFoundError,
)
from src.domain.dto.base import UserBaseSchema
from src.domain.dto.leagues_data.base.full_statistics import (
    FullStatisticsBaseSchema,
    GameInfoBaseSchema,
    PlayerProfileInfoBaseSchema,
    SeasonInfoBaseSchema,
    TeamInfoBaseSchema,
)
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.interfaces.gateways import FileStorage, ImageLoader
from src.domain.interfaces.gateways.database.unit_of_work import FullStatisticsSaverBaseUnitOfWork
from src.domain.use_cases.parsers.factory import ParserFactory
from src.utils import get_extension_from_url

if TYPE_CHECKING:
    from src.domain.use_cases.parsers.interface import LeagueParser


class FullStatisticsSaver:
    def __init__(
        self,
        parser_factory: ParserFactory,
        uow: FullStatisticsSaverBaseUnitOfWork,
        file_storage: FileStorage,
        image_loader: ImageLoader,
    ) -> None:
        self._parser_factory = parser_factory
        self.uow = uow
        self._file_storage = file_storage
        self._image_loader = image_loader

    async def _save_profile_photo(self, profile: PlayerProfileInfoBaseSchema, league: LeagueTypeEnum) -> None:
        if not profile.photo_url:
            return
        content = await self._image_loader.load(profile.photo_url.encoded_string())
        if not content:
            return
        ext = get_extension_from_url(profile.photo_url.encoded_string())
        file_key = f"{PROFILES_PATH}/{league.value}/{profile.profile_id}{ext}"
        await self._file_storage.save_file(BytesIO(content), file_key)
        profile.photo = file_key

    async def _save_team_logo(self, team: TeamInfoBaseSchema, league: LeagueTypeEnum) -> None:
        if not team.logo_url:
            return
        content = await self._image_loader.load(team.logo_url.encoded_string())
        if not content:
            return
        ext = get_extension_from_url(team.logo_url.encoded_string())
        file_key = f"{TEAMS_PATH}/{league.value}/{team.team_name}_{team.external_team_id}{ext}"
        await self._file_storage.save_file(BytesIO(content), file_key)
        team.logo = file_key

    async def _get_user_and_check_user_info(
        self, data_from_user: LeagueUrlsUserInputSchema, tg_id: int
    ) -> UserBaseSchema:
        if not (user := await self.uow.user_repo.get_user_by_tg_id(tg_id)):
            logger.info("Пользователь не найден", tg_id=tg_id)
            raise UserNotFoundError()
        if not await self.uow.user_agreement_repo.is_exists_by_user_id(user.user_id):
            logger.info("Согласие пользователя не найдено", user_id=user.user_id)
            raise UserAgreementNotFoundError()
        if await self.uow.player_profile_repo.is_exists(user.user_id, data_from_user.league_type):
            logger.info(
                "Профиль игрока для лиги уже существует",
                user_id=user.user_id,
                league_type=data_from_user.league_type,
            )
            raise PlayerProfileAlreadySavedError()
        return user

    async def _get_full_statistics(
        self, data_from_user: LeagueUrlsUserInputSchema, tg_id: int
    ) -> FullStatisticsBaseSchema:
        parser: LeagueParser = self._parser_factory.get_fast_statistics_parser(data_from_user)
        logger.debug(
            "Парсер выбран",
            league_type=data_from_user.league_type,
            parser_type=type(parser).__name__,
        )
        try:
            return await parser.get_full_statistics(data_from_user)
        except ValidationError as error:
            logger.error(
                "Ошибка валидации при получении полной статистики",
                tg_id=tg_id,
                league_type=data_from_user.league_type,
                error=str(error),
            )
            raise URLValidationException from error

    def _collect_all_teams(self, seasons: list[SeasonInfoBaseSchema]) -> list[TeamInfoBaseSchema]:
        teams: list[TeamInfoBaseSchema] = []
        for season in seasons:
            for division in season.divisions:
                teams.extend(division.teams)
        return teams

    async def _save_player_profile(
        self, player_profile: PlayerProfileInfoBaseSchema, league_type: LeagueTypeEnum, user: UserBaseSchema
    ) -> None:
        try:
            await self.uow.player_profile_repo.create(player_profile, user.user_id)
            logger.info(
                "Профиль игрока создан",
                tg_id=user.tg_id,
                user_id=user.user_id,
                league_type=league_type,
                player_profile_id=player_profile.player_profile_id,
            )
        except DuplicatedRecordException as db_error:
            logger.error(
                "Дубликат профиля игрока при сохранении",
                tg_id=user.tg_id,
                user_id=user.user_id,
                league_type=league_type,
            )
            raise PlayerProfileAlreadySavedError from db_error

    async def _save_seasons_divisions_teams(
        self, seasons: list[SeasonInfoBaseSchema], player_profile: PlayerProfileInfoBaseSchema
    ) -> None:
        logger.info(
            "Сохранение сезонов, дивизионов, команд",
            seasons_count=len(seasons),
        )
        for season in seasons:
            saved_season = await self.uow.season_repo.upsert(season)
            for league_season in season.league_seasons:
                await self.uow.league_season_repo.upsert(saved_season.season_id, league_season)
            for division in season.divisions:
                saved_division = await self.uow.division_repo.upsert(division, saved_season.season_id)
                for team in division.teams:
                    saved_team = await self.uow.team_repo.upsert(team)
                    await self.uow.team_division_repo.upsert(saved_team.team_id, saved_division.division_id)
                    await self.uow.player_team_repo.upsert(player_profile.player_profile_id, saved_team.team_id)

    async def _save_games_and_player_statistics(self, games: list[GameInfoBaseSchema]) -> None:
        logger.info(
            "Сохранение игр и статистки игрока",
            games_count=len(games),
        )
        for game in games:
            saved_game = await self.uow.game_repo.upsert(game)
            if game.player_statistics:
                game.player_statistics.game_id = saved_game.game_id
                await self.uow.player_game_statistics_repo.upsert(game.player_statistics)

    async def _save_images(self, full_statistics: FullStatisticsBaseSchema) -> None:
        save_photo_task = self._save_profile_photo(
            full_statistics.player_profile, full_statistics.player_profile.league
        )
        all_teams = self._collect_all_teams(full_statistics.seasons)
        save_logos_tasks = [self._save_team_logo(team, team.league) for team in all_teams]
        await asyncio.gather(save_photo_task, *save_logos_tasks)

    async def __call__(self, data_from_user: LeagueUrlsUserInputSchema, tg_id: int) -> None:
        logger.info(
            "Сохранение полной статистики запущено",
            tg_id=tg_id,
            league_type=data_from_user.league_type,
        )
        async with self.uow:
            user = await self._get_user_and_check_user_info(data_from_user, tg_id)
            full_statistics = await self._get_full_statistics(data_from_user, tg_id)
            logger.info(
                "Полная статистика получена",
                tg_id=tg_id,
                league_type=data_from_user.league_type,
            )

            await self._save_player_profile(full_statistics.player_profile, data_from_user.league_type, user)
            await self._save_seasons_divisions_teams(full_statistics.seasons, full_statistics.player_profile)
            await self._save_games_and_player_statistics(full_statistics.games)
            logger.info(
                "Полная статистика успешно сохранена",
                tg_id=tg_id,
                user_id=user.user_id,
                league_type=data_from_user.league_type,
                seasons_count=len(full_statistics.seasons),
                games_count=len(full_statistics.games),
            )
