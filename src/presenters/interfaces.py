from abc import ABC, abstractmethod
from functools import cached_property

from common.domain.dto.league_reader_input import LeagueTypeEnum
from common.domain.dto.statistics_presenter import StatisticsPresenterSchema
from src.domain.dto.base.league import LeagueBaseSchema


class MultiplyDataPresenter(ABC):
    @abstractmethod
    def __call__(self, data: tuple[StatisticsPresenterSchema, ...]) -> tuple[tuple[bytes, str], ...]:
        raise NotImplementedError


class LeagueInfoPresenterInterface(ABC):
    @cached_property
    @abstractmethod
    def all_leagues(self) -> tuple[LeagueBaseSchema, ...]:
        raise NotImplementedError

    @abstractmethod
    def get_league_by_id(self, league_id: int) -> LeagueBaseSchema:
        raise NotImplementedError

    @abstractmethod
    def get_league_type_by_fast_statistics(self, text: str) -> LeagueTypeEnum | None:
        raise NotImplementedError
