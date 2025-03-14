from common.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.use_cases.parsers.interface import LeagueParser


class ParserFactory:

    def __init__(self, parsers: dict[LeagueTypeEnum, LeagueParser]) -> None:
        self._parsers = parsers

    def get_fast_statistics_parser(self, data_from_user: LeagueUrlsUserInputSchema) -> LeagueParser:
        return self._parsers.get(data_from_user.league_type)
