from loguru import logger
from pydantic import ValidationError

from common.domain.dto.league_reader_input import LeagueTypeEnum
from common.domain.dto.statistics_presenter import PlayerStaticsPresenterSchema
from common.exceptions.parsers_exceptions import URLValidationException
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.use_cases.parsers.interface import LeagueParser


class ParserFactory:

    def __init__(
        self, mlbl_parser: LeagueParser, bcl_parser: LeagueParser, abl_parser: LeagueParser
    ) -> None:
        self._parsers: dict[LeagueTypeEnum, LeagueParser] = {
            LeagueTypeEnum.ABL: abl_parser,
            LeagueTypeEnum.BCL: bcl_parser,
            LeagueTypeEnum.MLBL: mlbl_parser,
        }

    async def parse_fast_statistic(
        self, data_from_user: LeagueUrlsUserInputSchema
    ) -> PlayerStaticsPresenterSchema:
        try:
            parser: LeagueParser = self._parsers[data_from_user.league_type]
            return await parser.parse_fast_statistic(data_from_user)
        except ValidationError as error:
            logger.error(error)
            raise URLValidationException()
