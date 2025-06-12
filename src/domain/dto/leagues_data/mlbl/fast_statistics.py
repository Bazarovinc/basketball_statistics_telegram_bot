from datetime import datetime

from pydantic import AliasPath, Field, field_validator, model_validator

from common.domain.dto.league_reader_input import LeagueTypeEnum
from common.domain.dto.statistics_presenter import (
    PlayerShortInfoBaseSchema,
    PlayerStaticsPresenterBaseSchema,
    StatisticPresenterBaseSchema,
)
from common.utils.date_parser import parse_date_from_timestamp
from src.constants import MAX_FAST_STATISTICS_GAMES_COUNT
from src.constants.fields import FIELDS_TO_ZERO
from src.constants.templates import GAME_INFO_TEMPLATE


class MLBLGameStatisticSchema(StatisticPresenterBaseSchema):
    game_date: datetime = Field(..., validation_alias=AliasPath("Game", "GameTime"))
    team_1_name: str = Field(..., validation_alias=AliasPath("TeamNameA", "CompTeamNameRu"))
    team_2_name: str = Field(..., validation_alias=AliasPath("TeamNameB", "CompTeamNameRu"))
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

    @field_validator("game_date", mode="before")
    def validate_game_date(cls, value: str | datetime) -> datetime:
        if isinstance(value, str):
            return parse_date_from_timestamp(value)
        return value

    @model_validator(mode="after")
    def set_game_info(self) -> "MLBLGameStatisticSchema":
        self.game_info = GAME_INFO_TEMPLATE.format(
            team_name_1=self.team_1_name,
            team_name_2=self.team_2_name,
            date=self.game_date.strftime("%d.%m.%Y %H:%M"),
        )
        return self


class MLBLPlayerFastStatisticsResponseSchema(PlayerShortInfoBaseSchema):
    first_name: str = Field(..., alias="PersonFirstNameRu")
    last_name: str = Field(..., alias="PersonLastNameRu")


class MLBLUserStatsPerGameResponseSchema(PlayerStaticsPresenterBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.MLBL
    player_info: MLBLPlayerFastStatisticsResponseSchema | None = None
    statistics_per_game: list[MLBLGameStatisticSchema] = Field(..., alias="GameStats")

    @field_validator("statistics_per_game", mode="after")
    def cut_games_statistics(
        cls, value: list[MLBLGameStatisticSchema]
    ) -> list[MLBLGameStatisticSchema]:
        return value[-MAX_FAST_STATISTICS_GAMES_COUNT:]
