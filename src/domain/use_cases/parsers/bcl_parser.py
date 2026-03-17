import asyncio
from collections import Counter

from bs4 import BeautifulSoup
from loguru import logger

from src.constants import BCL_PLAYER_SEASON_GAMES_ADDRESS, BCL_TEAM_ADDRESS
from src.core.exceptions.parsers_exceptions import ServerNotAvailableException
from src.domain.dto.leagues_data.bcl.fast_statistics import (
    BCLFastStatisticsSchema,
)
from src.domain.dto.leagues_data.bcl.full_statistics import (
    BCLFullStatisticsSchema,
    BCLPlayerSeasonSchema,
)
from src.domain.dto.leagues_data.bcl.reader_input import BCLInputBaseSchema
from src.domain.use_cases.parsers.interface import LeagueParser
from src.utils import (
    check_player_in_team,
    check_player_played_in_season,
    parse_bcl_player_profile,
    parse_current_season_name,
    parse_fast_statistics,
    parse_season_ids,
    parse_team_id,
)


class BCLParser(LeagueParser[BCLInputBaseSchema, BCLFastStatisticsSchema, BCLFullStatisticsSchema]):
    input_schema = BCLInputBaseSchema
    player_season_games_address: str = BCL_PLAYER_SEASON_GAMES_ADDRESS
    team_address: str = BCL_TEAM_ADDRESS

    async def get_fast_statistics(self, data_from_user: BCLInputBaseSchema) -> BCLFastStatisticsSchema:
        data_from_user = self._validate_input(data_from_user)
        html = await self._league_reader.get_data_html(data_from_user.player_url.unicode_string())
        if not html:
            logger.error("Данный от лиги не получены")
            raise ServerNotAvailableException()
        soup = BeautifulSoup(html, "html.parser")
        return parse_fast_statistics(soup)

    async def _choose_team_id(self, team_ids: Counter[int], player_id: str, season_id: int) -> int:
        for team_id, count in team_ids.most_common():
            if count == 2:
                html = await self._league_reader.get_data_html(
                    self.team_address.format(team_id=team_id, season_id=season_id)
                )
                if check_player_in_team(BeautifulSoup(html, "html.parser"), player_id):
                    return team_id

    async def _get_team_id_from_matches(
        self, player_season_page: BeautifulSoup, player_id: str, season_id
    ) -> int | None:
        counter = parse_team_id(player_season_page)
        team_id, count = counter.most_common(1)[0]
        if count == 2:
            return await self._choose_team_id(counter, player_id, season_id)
        return team_id

    async def _get_played_seasons(self, seasons: list[int], player_id: str) -> tuple[BCLPlayerSeasonSchema, ...]:
        tasks = tuple(
            [
                self._league_reader.get_data_html(
                    self.player_season_games_address.format(season_id=season, player_id=player_id)
                )
                for season in seasons
            ]
        )
        result: list[BCLPlayerSeasonSchema] = []
        for player_season_html, season_id in zip(await asyncio.gather(*tasks), seasons):
            player_season_page = BeautifulSoup(player_season_html, "html.parser")
            if check_player_played_in_season(player_season_page):
                team_id = await self._get_team_id_from_matches(player_season_page, player_id, season_id)
                result.append(
                    BCLPlayerSeasonSchema(
                        season_id=season_id, team_id=team_id, season_name=parse_current_season_name(player_season_page)
                    )
                )
        return tuple(result)

    async def get_full_statistics(self, data_from_user: BCLInputBaseSchema) -> BCLFullStatisticsSchema:
        data_from_user = self._validate_input(data_from_user)
        html = await self._league_reader.get_data_html(data_from_user.player_url.unicode_string())
        if not html:
            logger.error("Данный от лиги не получены")
            raise ServerNotAvailableException()
        soup = BeautifulSoup(html, "html.parser")
        played_seasons = await self._get_played_seasons(parse_season_ids(soup), data_from_user.player_id)
        teams_pages_html = await asyncio.gather(
            *[
                self._league_reader.get_data_html(
                    self.team_address.format(season_id=played_season.season_id, team_id=played_season.team_id)
                )
                for played_season in played_seasons
            ]
        )
        player_profile = parse_bcl_player_profile(soup, data_from_user.player_id)
