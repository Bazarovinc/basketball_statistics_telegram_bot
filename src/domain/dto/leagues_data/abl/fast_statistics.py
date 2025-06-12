from datetime import datetime

from pydantic import AliasPath, Field

from common.domain.dto import BaseSchema
from common.domain.dto.league_reader_input import LeagueTypeEnum
from common.domain.dto.statistics_presenter import (
    PlayerShortInfoBaseSchema,
    PlayerStaticsPresenterBaseSchema,
    StatisticPresenterBaseSchema,
)
from src.constants import GAME_INFO_TEMPLATE


class ABLGameStatisticsSchema(StatisticPresenterBaseSchema):
    game_user_id: int
    game_info: str | None = None
    player_number: int | None = None
    total_points: int | None = Field(..., alias="points")
    points_1: int | None = Field(..., alias="free_throws_made")
    shots_1: int | None = Field(..., alias="free_throw_attempts")
    shots_1_percent: float | None = Field(..., alias="free_throw_percent")
    points_2: int | None = Field(..., alias="two_points_made")
    shots_2: int | None = Field(..., alias="two_point_attempts")
    shots_2_percent: float | None = Field(..., alias="two_point_percent")
    points_3: int | None = Field(..., alias="three_points_made")
    shots_3: int | None = Field(..., alias="three_point_attempts")
    shots_3_percent: float | None = Field(..., alias="three_point_percent")
    assists: int | None
    blocks: int | None
    defence_rebounds: int | None = Field(..., alias="defensive_rebounds")
    offence_rebounds: int | None = Field(..., alias="offensive_rebounds")
    steals: int | None
    turnovers: int | None
    fouls: int | None = Field(..., alias="personal_fouls")
    opponent_fouls: int | None = Field(..., alias="drawn_fouls")
    played_time: int | None = Field(None, alias="game_time")
    plus_minus: int | None
    is_start: bool | None = None
    kpi: int | None = Field(..., alias="player_efficiency")


class ABLPlayerFastStatisticsResponseSchema(PlayerShortInfoBaseSchema):
    user_id: int
    first_name: str
    last_name: str


class ABLFSGameInfoResponseSchema(BaseSchema):
    id: int
    left_team_name: str = Field(..., validation_alias=AliasPath("competitor_team", "name"))
    right_team_name: str = Field(..., validation_alias=AliasPath("team", "name"))
    game_date: datetime = Field(..., alias="datetime")

    @property
    def game_info(self) -> str:
        return GAME_INFO_TEMPLATE.format(
            team_name_1=self.left_team_name,
            team_name_2=self.right_team_name,
            date=self.game_date.strftime("%d.%m.%Y %H:%M"),
        )


class ABLPlayerGameInfoResponseSchema(BaseSchema):
    id: int
    player_id: int = Field(..., validation_alias=AliasPath("team_user", "user", "id"))
    player_number: int | None = Field(None, alias="number")


class ABLUserStatsPerGameResponseSchema(PlayerStaticsPresenterBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.ABL
    player_info: ABLPlayerFastStatisticsResponseSchema | None = None
    statistics_per_game: list[ABLGameStatisticsSchema]
