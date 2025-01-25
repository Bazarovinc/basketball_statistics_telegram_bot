from pydantic import Field, field_validator, model_validator

from common.domain.dto.league_reader_input import LeagueTypeEnum
from common.domain.dto.statistics_presenter import (
    PlayerShortInfoBaseSchema,
    PlayerStaticsPresenterBaseSchema,
    StatisticPresenterBaseSchema,
)


class BCLGameStatisticSchema(StatisticPresenterBaseSchema):
    game_info: str = Field(..., alias="Матч")
    total_points: int = Field(..., alias="Очки")
    points_1: int | None = 0
    shots_1: int | None = 0
    shots_1_percent: float | None = 0
    shots_1_percent_name: str = Field(..., alias="1x %")
    points_2: int | None = 0
    shots_2: int | None = 0
    shots_2_percent: float | None = 0
    shots_2_percent_name: str = Field(..., alias="2x %")
    points_3: int | None = 0
    shots_3: int | None = 0
    shots_3_percent: float | None = 0
    shots_3_percent_name: str = Field(..., alias="3x %")
    assists: int | None = Field(..., alias="ПР")
    blocks: int | None = Field(..., alias="БШ")
    defence_rebounds: int | None = Field(..., alias="СЩ")
    offence_rebounds: int | None = Field(..., alias="ЧЩ")
    steals: int | None = Field(..., alias="ПХ")
    turnovers: int | None = Field(..., alias="ПТ")
    fouls: int | None = Field(..., alias="Ф")
    opponent_fouls: int | None = Field(..., alias="ФС")
    played_time: str | None = Field(..., alias="ВР")
    plus_minus: int | None = None
    is_start_str: str | None = Field(..., alias="F5")
    is_start: bool | None = False
    kpi: int | None = Field(..., alias="КП")

    @field_validator("game_info", mode="after")
    def reform_game_info(cls, value: str) -> str:
        return ":".join((team.strip() for team in value.split("-")))

    @model_validator(mode="after")
    def parse_shots(self) -> "BCLGameStatisticSchema":

        shots_1, percent_1 = self.shots_1_percent_name.split()
        shots_1 = (int(i) for i in shots_1.split("/"))
        self.points_1, self.shots_1 = shots_1
        self.shots_1_percent = float(percent_1[1:-2])

        shots_2, percent_2 = self.shots_2_percent_name.split()
        shots_2 = (int(i) for i in shots_2.split("/"))
        self.points_2, self.shots_2 = shots_2
        self.shots_2_percent = float(percent_2[1:-2])

        shots_3, percent_3 = self.shots_3_percent_name.split()
        shots_3 = (int(i) for i in shots_3.split("/"))
        self.points_3, self.shots_3 = shots_3
        self.shots_3_percent = float(percent_3[1:-2])

        if self.is_start_str == "√":
            self.is_start = True
        return self


class BCLPlayerFastStatisticsResponseSchema(PlayerShortInfoBaseSchema):
    first_name: str
    last_name: str


class BCLUserStatsPerGameResponseSchema(PlayerStaticsPresenterBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.BCL
    player_info: BCLPlayerFastStatisticsResponseSchema
    statistics_per_game: list[BCLGameStatisticSchema]
