from abc import ABC, abstractmethod
from functools import cached_property

from common.domain.dto.statistics_presenter import StatisticPresenterSchema
from src.domain.dto.base.league import LeagueBaseSchema, ScreenshotSchema


class MultiplyDataPresenter(ABC):

    @abstractmethod
    def __call__(self, data: tuple[StatisticPresenterSchema, ...]) -> tuple[tuple[bytes, str], ...]:
        raise NotImplementedError


class LeagueInfoPresenterInterface(ABC):

    @cached_property
    @abstractmethod
    def all_leagues(self) -> tuple[LeagueBaseSchema, ...]:
        raise NotImplementedError

    @abstractmethod
    def get_league_by_id(self, league_id: int) -> LeagueBaseSchema:
        raise NotImplementedError

    @cached_property
    @abstractmethod
    def default_tutorial(self) -> tuple[ScreenshotSchema, ...]:
        raise NotImplementedError
