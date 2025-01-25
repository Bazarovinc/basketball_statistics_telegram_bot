from abc import ABC, abstractmethod

from common.domain.dto.league_reader_input import LeagueInputSchema
from common.domain.dto.statistics_presenter import PlayerStaticsPresenterSchema
from common.getaways.league_reader import LeagueReaderInterface


class LeagueParser(ABC):

    def __init__(self, league_reader: LeagueReaderInterface) -> None:
        self._league_reader = league_reader

    # @abstractmethod
    # async def parse_full_player_info(self, data_from_user: Type[LeagueInputSchema]):
    #     raise NotImplementedError

    @abstractmethod
    async def parse_fast_statistic(
        self, data_from_user: LeagueInputSchema
    ) -> PlayerStaticsPresenterSchema:
        raise NotImplementedError
