from functools import cached_property

from common.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.dto.base.league import LEAGUES, LeagueBaseSchema
from src.presenters.interfaces import LeagueInfoPresenterInterface


class LeagueInfoPresenter(LeagueInfoPresenterInterface):
    leagues: dict[int, LeagueBaseSchema] = LEAGUES

    @cached_property
    def all_leagues(self) -> tuple[LeagueBaseSchema, ...]:
        return tuple(value for value in self.leagues.values())

    def get_league_by_id(self, league_id: int) -> LeagueBaseSchema:
        if league := self.leagues.get(league_id):
            return league
        raise KeyError(f"Лига с id {league_id} не найдена")

    def get_league_type_by_fast_statistics(self, text: str) -> LeagueTypeEnum | None:
        for league_info in self.leagues.values():
            if league_info.fast_statistics_info.profile_link.unicode_string() in text:
                return league_info.league_type
        return None
