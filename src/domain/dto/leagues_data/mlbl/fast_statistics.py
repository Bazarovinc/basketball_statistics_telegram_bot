from datetime import datetime

from pydantic import Field, field_validator, model_validator

from common.domain.dto import BaseSchema
from common.domain.dto.league_reader_input import LeagueTypeEnum
from common.domain.dto.statistics_presenter import (
    PlayerShortInfoBaseSchema,
    PlayerStaticsPresenterBaseSchema,
    StatisticPresenterBaseSchema,
)
from common.utils.date_parser import parse_date_from_timestamp
from src.constants.fields import FIELDS_TO_ZERO
from src.constants.templates import GAME_INFO_TEMPLATE


class MLBLGameInfoSchema(BaseSchema):
    game_date: datetime = Field(..., alias="GameTime")

    @field_validator("game_date", mode="before")
    def validate_datetime(cls, value: str | datetime) -> datetime:
        if isinstance(value, str):
            return parse_date_from_timestamp(value)
        return value


class MLBTeamInfoSchema(BaseSchema):
    team_name: str = Field(..., alias="CompTeamNameRu")


class MLBLGameStatisticSchema(StatisticPresenterBaseSchema):
    game_info: str | None = None
    game: MLBLGameInfoSchema = Field(..., alias="Game")
    team_1: MLBTeamInfoSchema = Field(..., alias="TeamNameA")
    team_2: MLBTeamInfoSchema = Field(..., alias="TeamNameB")
    player_number: int = Field(..., alias="PlayerNumber")
    total_points: int | None = Field(..., alias="Points")
    points_1: int | None = Field(..., alias="Goal1")
    shots_1: int | None = Field(..., alias="Shot1")
    points_2: int | None = Field(..., alias="Goal2")
    shots_2: int | None = Field(..., alias="Shot2")
    points_3: int | None = Field(..., alias="Goal3")
    shots_3: int | None = Field(..., alias="Shot3")
    assists: int | None = Field(..., alias="Assist")
    blocks: int | None = Field(..., alias="Blocks")
    defence_rebounds: int | None = Field(..., alias="DefRebound")
    offence_rebounds: int | None = Field(..., alias="OffRebound")
    steals: int | None = Field(..., alias="Steal")
    turnovers: int | None = Field(..., alias="Turnover")
    fouls: int | None = Field(..., alias="Foul")
    opponent_fouls: int | None = Field(..., alias="OpponentFoul")
    played_time: str | None = Field(..., alias="PlayedTime")
    plus_minus: int | None = Field(..., alias="PlusMinus")
    is_start: bool | None = Field(..., alias="IsStart")
    kpi: int | None = Field(..., alias="KPI")

    @field_validator(
        "kpi",
        *FIELDS_TO_ZERO,
        mode="after",
    )
    def set_zero(cls, value: int | None) -> int:
        if value is None:
            return 0
        return value

    @model_validator(mode="after")
    def set_game_info(self) -> "MLBLGameStatisticSchema":
        self.game_info = GAME_INFO_TEMPLATE.format(
            team_name_1=self.team_1.team_name,
            team_name_2=self.team_2.team_name,
            date=self.game.game_date.strftime("%d.%m.%Y %H:%M"),
        )
        return self


class MLBLPlayerFastStatisticsResponseSchema(PlayerShortInfoBaseSchema):
    first_name: str = Field(..., alias="PersonFirstNameRu")
    last_name: str = Field(..., alias="PersonLastNameRu")


class MLBLUserStatsPerGameResponseSchema(PlayerStaticsPresenterBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.MLBL
    player_info: MLBLPlayerFastStatisticsResponseSchema | None = None
    statistics_per_game: list[MLBLGameStatisticSchema] = Field(..., alias="GameStats")
