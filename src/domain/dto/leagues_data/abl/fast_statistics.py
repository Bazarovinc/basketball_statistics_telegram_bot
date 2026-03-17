from datetime import datetime, timedelta
from functools import cached_property

from pydantic import AliasChoices, AliasPath, Field, computed_field
from typing_extensions import override

from src.constants import GAME_INFO_TEMPLATE
from src.core.domain.dto import (
    BaseSchema,
    PlayerShortInfoBaseSchema,
    PlayerStatisticsPresenterBaseSchema,
    StatisticsPresenterBaseSchema,
)
from src.core.domain.dto.league_reader_input import LeagueTypeEnum


class ABLGameStatisticsSchema(StatisticsPresenterBaseSchema):
    game_user_id: int
    game_info: str | None = None
    player_number: int | None = None
    total_points: int = Field(..., alias="points")
    points_1: int = Field(..., alias="free_throws_made")
    shots_1: int = Field(..., alias="free_throw_attempts")
    shots_1_percent: float = Field(..., alias="free_throw_percent")
    points_2: int = Field(..., alias="two_points_made")
    shots_2: int = Field(..., alias="two_point_attempts")
    shots_2_percent: float = Field(..., alias="two_point_percent")
    points_3: int = Field(..., alias="three_points_made")
    shots_3: int = Field(..., alias="three_point_attempts")
    shots_3_percent: float = Field(..., alias="three_point_percent")
    assists: int
    blocks: int
    defence_rebounds: int = Field(..., alias="defensive_rebounds")
    offence_rebounds: int = Field(..., alias="offensive_rebounds")
    steals: int
    turnovers: int
    fouls: int = Field(..., alias="personal_fouls")
    opponent_fouls: int = Field(..., alias="drawn_fouls")
    played_time: int | None = Field(None, alias="game_time")
    plus_minus: int
    is_start: bool | None = None
    kpi: int = Field(..., alias="player_efficiency")
    game_date: datetime | None = Field(None, exclude=True)

    @override
    @computed_field
    @cached_property
    def played_time_seconds(self) -> timedelta:
        return timedelta(seconds=self.played_time if self.played_time else 0)


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
    # Сначала номер из tournament_team_user (последний в JSON), при отсутствии — из team_user
    player_number: int | None = Field(
        None,
        validation_alias=AliasChoices(
            "number",
            AliasPath("team_user", "number"),
        ),
    )


class ABLFastStatisticsSchema(PlayerStatisticsPresenterBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.ABL
    player_info: ABLPlayerFastStatisticsResponseSchema | None = None
    statistics_per_game: list[ABLGameStatisticsSchema]
