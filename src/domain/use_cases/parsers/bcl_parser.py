from bs4 import BeautifulSoup
from loguru import logger

from common.exceptions.parsers_exceptions import ServerNotAvailableException
from src.domain.dto.leagues_data.bcl.fast_statistics import (
    BCLFastStatisticsSchema,
)
from src.domain.dto.leagues_data.bcl.reader_input import BCLInputBaseSchema
from src.domain.use_cases.parsers.interface import LeagueParser
from src.utils import parse_matches_table, parse_player_info

# Порядок колонок в таблице «Матчи» на странице игрока (актуальный HTML)


class BCLParser(LeagueParser[BCLInputBaseSchema]):
    input_schema = BCLInputBaseSchema

    async def get_fast_statistics(self, data_from_user: BCLInputBaseSchema) -> BCLFastStatisticsSchema:
        data_from_user = self._validate_input(data_from_user)
        html = await self._league_reader.get_data_html(data_from_user.player_url.unicode_string())
        if not html:
            logger.error("Данный от лиги не получены")
            raise ServerNotAvailableException()
        soup = BeautifulSoup(html, "html.parser")
        player_info = parse_player_info(soup)
        game_statistics = parse_matches_table(soup)
        return BCLFastStatisticsSchema(player_info=player_info, statistics_per_game=game_statistics)
