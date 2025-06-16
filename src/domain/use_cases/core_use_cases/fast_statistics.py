from loguru import logger
from pydantic_core._pydantic_core import ValidationError

from common.exceptions.parsers_exceptions import URLValidationException
from src.domain.dto.outputs.fast_statistics import FastStatisticsOutputSchema
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.use_cases.parsers.factory import ParserFactory
from src.domain.use_cases.parsers.interface import LeagueParser
from src.presenters.interfaces import MultiplyDataPresenter


class FastStatisticsGetter:

    def __init__(self, parser_factory: ParserFactory, presenter: MultiplyDataPresenter) -> None:
        self._parser_factory = parser_factory
        self._presenter = presenter

    async def __call__(self, data_from_user: LeagueUrlsUserInputSchema) -> FastStatisticsOutputSchema:
        logger.info("Вызов логики для получения быстрой статистики")
        parser: LeagueParser = self._parser_factory.get_fast_statistics_parser(data_from_user)
        try:
            player_stats = await parser.parse_fast_statistic(data_from_user)
        except ValidationError as error:
            logger.error(error)
            raise URLValidationException()
        return FastStatisticsOutputSchema(
            images=self._presenter(player_stats.statistics_per_game),
            username=player_stats.player_info.username,
            league=player_stats.league,
        )
