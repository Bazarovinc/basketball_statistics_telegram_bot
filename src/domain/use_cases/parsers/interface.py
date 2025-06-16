from abc import ABC, abstractmethod
from typing import Generic, Type

from common.domain.dto.league_reader_input import LeagueInputSchema, LeagueReaderInputSchema
from common.domain.dto.statistics_presenter import PlayerStaticsPresenterSchema
from common.getaways.league_reader import LeagueReaderInterface


class LeagueParser(ABC, Generic[LeagueInputSchema]):

    input_schema: Type[LeagueInputSchema]

    def __init__(self, league_reader: LeagueReaderInterface) -> None:
        self._league_reader = league_reader

    # @abstractmethod
    # async def parse_full_player_info(self, data_from_user: Type[LeagueInputSchema]):
    #     raise NotImplementedError

    def _validate_input(self, data: LeagueReaderInputSchema) -> LeagueInputSchema:
        return self.input_schema(**data.model_dump())

    @abstractmethod
    async def parse_fast_statistic(self, data_from_user: LeagueInputSchema) -> PlayerStaticsPresenterSchema:
        raise NotImplementedError
