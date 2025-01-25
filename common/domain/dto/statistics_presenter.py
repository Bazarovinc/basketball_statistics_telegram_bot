from functools import cached_property
from typing import TypeVar

from common.domain.dto import BaseSchema
from common.domain.dto.league_reader_input import LeagueTypeEnum


class StatisticPresenterBaseSchema(BaseSchema):
    game_info: str | None = None
    total_points: int | None
    points_1: int | None
    shots_1: int | None
    # shots_1_percent: int | None = None
    # shots_1_percent_name: str | None = None
    points_2: int | None
    shots_2: int | None
    # shots_2_percent: int | None = None
    # shots_2_percent_name: str | None = None
    points_3: int | None
    shots_3: int | None
    # shots_3_percent: int | None = None
    # shots_3_percent_name: str | None = None
    assists: int | None
    blocks: int | None
    defence_rebounds: int | None
    offence_rebounds: int | None
    steals: int | None
    turnovers: int | None
    fouls: int | None
    opponent_fouls: int | None
    played_time: str | None
    plus_minus: int | None
    is_start: bool | None
    kpi: int | None


class PlayerShortInfoBaseSchema(BaseSchema):
    first_name: str
    last_name: str

    @cached_property
    def username(self) -> str:
        return self.last_name + " " + self.first_name


class PlayerStaticsPresenterBaseSchema(BaseSchema):
    league: LeagueTypeEnum
    player_info: PlayerShortInfoBaseSchema
    statistics_per_game: tuple[StatisticPresenterBaseSchema]


StatisticPresenterSchema = TypeVar("StatisticPresenterSchema", bound=StatisticPresenterBaseSchema)
PlayerStaticsPresenterSchema = TypeVar(
    "PlayerStaticsPresenterSchema", bound=PlayerStaticsPresenterBaseSchema
)
