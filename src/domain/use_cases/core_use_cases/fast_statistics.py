from loguru import logger

from src.domain.dto.outputs.fast_statistics import FastStatisticsOutputSchema
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.use_cases.parsers.factory import ParserFactory
from src.presenters.interfaces import MultiplyDataPresenter


class FastStatisticsGetter:

    def __init__(self, parser_factory: ParserFactory, presenter: MultiplyDataPresenter) -> None:
        self._parser_factory = parser_factory
        self._presenter = presenter

    async def __call__(
        self, data_from_user: LeagueUrlsUserInputSchema
    ) -> FastStatisticsOutputSchema:
        logger.info("Вызов логики для получения быстрой статистики")
        player_stats = await self._parser_factory.parse_fast_statistic(data_from_user)
        return FastStatisticsOutputSchema(
            images=self._presenter(player_stats.statistics_per_game),
            username=player_stats.player_info.username,
            league=player_stats.league,
        )
