from abc import ABC, abstractmethod
from typing import Generic

from src.core.domain.dto import PlayerStatisticsPresenterSchema
from src.core.domain.dto.league_reader_input import LeagueInputSchema, LeagueReaderInputSchema
from src.domain.dto.leagues_data.base import FullStatisticsSchema
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.interfaces.gateways.league_reader import LeagueReaderInterface


class LeagueParser(
    ABC,
    Generic[LeagueInputSchema, PlayerStatisticsPresenterSchema, FullStatisticsSchema],
):
    input_schema: type[LeagueInputSchema]

    def __init__(self, league_reader: LeagueReaderInterface) -> None:
        self._league_reader = league_reader

    def __str__(self) -> str:
        return self.__class__.__name__

    def _validate_input(self, data: LeagueReaderInputSchema) -> LeagueInputSchema:
        return self.input_schema(**data.model_dump())

    @abstractmethod
    async def get_fast_statistics(self, data_from_user: LeagueUrlsUserInputSchema) -> PlayerStatisticsPresenterSchema:
        raise NotImplementedError

    @abstractmethod
    async def get_full_statistics(self, data_from_user: LeagueUrlsUserInputSchema) -> FullStatisticsSchema:
        raise NotImplementedError
