from functools import cached_property

from src.domain.dto.base.league import (
    FAST_STATISTICS_DEFAULT_TUTORIAL_SCREENSHOTS,
    LEAGUES,
    LeagueBaseSchema,
    ScreenshotSchema,
)
from src.presenters.interfaces import LeagueInfoPresenterInterface


class LeagueInfoPresenter(LeagueInfoPresenterInterface):

    leagues: dict[int, LeagueBaseSchema] = LEAGUES

    @cached_property
    def all_leagues(self) -> tuple[LeagueBaseSchema, ...]:
        return tuple((value for value in self.leagues.values()))

    def get_league_by_id(self, league_id: int) -> LeagueBaseSchema:
        if league := self.leagues.get(league_id):
            return league
        raise KeyError(f"Лига с id {league_id} не найдена")

    @cached_property
    def default_tutorial(self) -> tuple[ScreenshotSchema, ...]:
        return FAST_STATISTICS_DEFAULT_TUTORIAL_SCREENSHOTS
