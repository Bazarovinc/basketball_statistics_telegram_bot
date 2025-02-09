import asyncio
from typing import Any

from loguru import logger
from pydantic import TypeAdapter

from common.domain.dto.statistics_presenter import PlayerStaticsPresenterSchema
from common.exceptions.parsers_exceptions import ServerNotAvailableException
from src.constants import (
    ABL_GAME_USERS_ADDRESS,
    ABL_GAME_USERS_STATISTICS_ADDRESS,
    ABL_PLAYED_GAMES_ADDRESS,
    ABL_PLAYER_PROFILE_ADDRESS,
)
from src.domain.dto.leagues_data.abl.fast_statistics import (
    ABLFSGameInfoResponseSchema,
    ABLGameStatisticsSchema,
    ABLPlayerFastStatisticsResponseSchema,
    ABLPlayerGameInfoResponseSchema,
    ABLUserStatsPerGameResponseSchema,
)
from src.domain.dto.leagues_data.abl.reader_input import ABLInputBaseSchema
from src.domain.use_cases.parsers.interface import LeagueParser


class ABLParser(LeagueParser[ABLInputBaseSchema]):
    input_schema = ABLInputBaseSchema
    player_profile_address: str = ABL_PLAYER_PROFILE_ADDRESS
    played_games_address: str = ABL_PLAYED_GAMES_ADDRESS
    game_users_address: str = ABL_GAME_USERS_ADDRESS
    game_users_statistics_address: str = ABL_GAME_USERS_STATISTICS_ADDRESS

    async def _get_player_games_statistics(
        self, games_info: list[ABLFSGameInfoResponseSchema]
    ) -> tuple[tuple[Any, ...], tuple[Any, ...]]:
        players_info_tasks, players_statistics_tasks = [], []
        for game_info in games_info:
            players_info_tasks.append(
                self._league_reader.get_data_json(
                    self.game_users_address.format(game_id=game_info.id)
                )
            )
            players_statistics_tasks.append(
                self._league_reader.get_data_json(
                    self.game_users_statistics_address.format(game_id=game_info.id)
                )
            )
        return await asyncio.gather(
            *(asyncio.gather(*players_info_tasks), asyncio.gather(*players_statistics_tasks))
        )

    def _match_player_statistics(
        self,
        player_profile: ABLPlayerFastStatisticsResponseSchema,
        games_info: list[ABLFSGameInfoResponseSchema],
        games_players_info: tuple[list[ABLPlayerGameInfoResponseSchema], ...],
        games_players_statistics: tuple[list[ABLGameStatisticsSchema], ...],
    ) -> list[ABLGameStatisticsSchema]:
        player_games_statistics: list[ABLGameStatisticsSchema] = []
        for game_players_info, game_players_statistics, game_info in zip(
            games_players_info, games_players_statistics, games_info
        ):
            # if not all((player_profile_response, games_info_response)):
            need_player: ABLPlayerGameInfoResponseSchema | None = None
            for player_info in game_players_info:
                if not player_info:
                    logger.error("Данные от лиги не получены")
                    raise ServerNotAvailableException()
                if player_info.player_id == player_profile.user_id:
                    need_player = player_info
                    break
            for players_statistics in game_players_statistics:
                if not players_statistics:
                    logger.error("Данные от лиги не получены")
                    raise ServerNotAvailableException()
                if need_player.id == players_statistics.game_user_id:
                    players_statistics.game_info = game_info.game_info
                    player_games_statistics.append(players_statistics)
        return player_games_statistics

    async def parse_fast_statistic(
        self, data_from_user: ABLInputBaseSchema
    ) -> PlayerStaticsPresenterSchema:
        data_from_user = self._validate_input(data_from_user)
        player_profile_response, games_info_response = await asyncio.gather(
            *(
                self._league_reader.get_data_json(
                    self.player_profile_address.format(player_id=data_from_user.player_id)
                ),
                self._league_reader.get_data_json(
                    self.played_games_address.format(
                        player_id=data_from_user.player_id, season_id=data_from_user.season_id
                    )
                ),
            )
        )
        if not all((player_profile_response, games_info_response)):
            logger.error("Данные от лиги не получены")
            raise ServerNotAvailableException()
        player_profile = ABLPlayerFastStatisticsResponseSchema(**player_profile_response)
        games_info = TypeAdapter(list[ABLFSGameInfoResponseSchema]).validate_python(
            games_info_response
        )
        games_players_info_response, games_players_statistics_response = (
            await self._get_player_games_statistics(games_info)
        )
        games_players_info = TypeAdapter(
            tuple[list[ABLPlayerGameInfoResponseSchema], ...]
        ).validate_python(games_players_info_response)
        games_players_statistics = TypeAdapter(
            tuple[list[ABLGameStatisticsSchema], ...]
        ).validate_python(games_players_statistics_response)
        return ABLUserStatsPerGameResponseSchema(
            player_info=player_profile,
            statistics_per_game=self._match_player_statistics(
                player_profile, games_info, games_players_info, games_players_statistics
            ),
        )
