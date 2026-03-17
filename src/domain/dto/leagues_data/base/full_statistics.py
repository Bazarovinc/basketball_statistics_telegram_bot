import json
import uuid
from datetime import date, datetime
from typing import Self, TypeVar

from pydantic import UUID4, AnyHttpUrl, Field, computed_field, model_validator

from src.constants import (
    CURRENT_SEASON_END_MONTH,
    CURRENT_SEASON_MID_MONTH,
    CURRENT_SEASON_START_MONTH,
    MOSCOW_TIMEZONE,
    SEASON_NAME_TEMPLATE,
)
from src.core.domain.dto import BaseSchema
from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.enums import GameStatusEnum, PositionEnum, GameQuarterEnum


class PlayerProfileInfoBaseSchema(BaseSchema):
    player_profile_id: UUID4 = Field(..., default_factory=uuid.uuid4)
    profile_id: str
    first_name: str
    last_name: str
    middle_name: str | None
    player_height: int | None
    player_weight: int | None
    birthdate: date | None = None
    position: PositionEnum | None = None
    player_rank: int | None = None
    photo: str | None = None
    photo_url: AnyHttpUrl | None = Field(None, exclude=True)
    player_number: int | None = None
    league: LeagueTypeEnum
    parse_date: datetime = Field(..., default_factory=lambda: datetime.now(MOSCOW_TIMEZONE))


class TeamInfoBaseSchema(BaseSchema):
    team_id: UUID4 = Field(..., default_factory=uuid.uuid4)
    external_team_id: str
    team_name: str
    team_short_name: str | None = None
    team_name_abc: str | None = None
    region: str | None = None
    logo: str | None = None
    logo_url: AnyHttpUrl | None = Field(None, exclude=True)
    league: LeagueTypeEnum


class DivisionInfoBaseSchema(BaseSchema):
    division_id: UUID4 = Field(..., default_factory=uuid.uuid4)
    external_division_id: str
    name: str
    league: LeagueTypeEnum
    teams: list[TeamInfoBaseSchema]


class LeagueSeasonInfoBaseSchema(BaseSchema):
    league_season_id: UUID4 = Field(..., default_factory=uuid.uuid4)
    external_season_id: str
    name: str
    league: LeagueTypeEnum


class SeasonInfoBaseSchema(BaseSchema):
    season_id: UUID4 = Field(..., default_factory=uuid.uuid4)
    name: str
    start_year: int
    end_year: int
    league_seasons: list[LeagueSeasonInfoBaseSchema] = Field(..., min_length=1, max_length=2)
    divisions: list[DivisionInfoBaseSchema]

    @model_validator(mode="after")
    def set_season_name(self) -> Self:
        self.name = SEASON_NAME_TEMPLATE.format(start_year=self.start_year, end_year=self.end_year)
        return self

    @computed_field
    @property
    def current_season(self) -> bool:
        current_date = datetime.now(MOSCOW_TIMEZONE)
        return (
            CURRENT_SEASON_START_MONTH <= current_date.month < CURRENT_SEASON_MID_MONTH
            and current_date.year == self.end_year
            or CURRENT_SEASON_MID_MONTH <= current_date.month <= CURRENT_SEASON_END_MONTH
            and current_date.year == self.start_year
        )


class PlayerGameStatisticsInfoBaseSchema(BaseSchema):
    player_game_statistics_id: UUID4 = Field(..., default_factory=uuid.uuid4)
    player_profile_id: UUID4
    game_id: UUID4
    player_number: int | None = None
    total_points: int = Field(0, ge=0, le=1000)
    points_1: int = Field(0, ge=0, le=100)
    shots_1: int = Field(0, ge=0, le=100)
    points_2: int = Field(0, ge=0, le=100)
    shots_2: int = Field(0, ge=0, le=100)
    points_3: int = Field(0, ge=0, le=100)
    shots_3: int = Field(0, ge=0, le=100)
    assists: int = Field(0, ge=0, le=100)
    blocks: int = Field(0, ge=0, le=100)
    defence_rebounds: int = Field(0, ge=0, le=100)
    offence_rebounds: int = Field(0, ge=0, le=100)
    steals: int = Field(0, ge=0, le=100)
    turnovers: int = Field(0, ge=0, le=100)
    fouls: int = Field(0, ge=0, le=7)
    opponent_fouls: int = Field(0, ge=0, le=100)
    played_time_seconds: int = Field(0, ge=0, le=7200)
    plus_minus: int = Field(0, ge=-500, le=500)
    is_start: bool = False
    kpi: int = Field(0, ge=-500, le=500)


class GameInfoBaseSchema(BaseSchema):
    game_id: UUID4 = Field(..., default_factory=uuid.uuid4)
    external_game_id: str
    division_id: UUID4 | None = None
    external_division_id: str | None = None
    left_team_id: UUID4 | None = None
    external_left_team_id: str | None = None
    right_team_id: UUID4 | None = None
    external_right_team_id: str | None = None
    left_team_name: str
    right_team_name: str
    game_date: datetime | None = None
    left_team_points: int | None = Field(0, ge=0)
    right_team_points: int | None = Field(0, ge=0)
    left_team_quarters_points: dict[GameQuarterEnum, int] | None = Field(default_factory=dict)
    right_team_quarters_points: dict[GameQuarterEnum, int] | None = Field(default_factory=dict)
    game_status: GameStatusEnum = GameStatusEnum.scheduled
    game_place: str | None = None
    competition: str | None = None
    player_statistics: PlayerGameStatisticsInfoBaseSchema

    @property
    def left_team_quarters_points_serialized(self) -> str:
        return json.dumps({str(k): v for k, v in self.left_team_quarters_points.items()})

    @property
    def right_team_quarters_points_serialized(self) -> str:
        return json.dumps({str(k): v for k, v in self.right_team_quarters_points.items()})


class FullStatisticsBaseSchema(BaseSchema):
    player_profile: PlayerProfileInfoBaseSchema
    seasons: list[SeasonInfoBaseSchema]
    games: list[GameInfoBaseSchema]


PlayerProfileInfoSchema = TypeVar("PlayerProfileInfoSchema", bound=PlayerProfileInfoBaseSchema)
TeamInfoSchema = TypeVar("TeamInfoSchema", bound=TeamInfoBaseSchema)
DivisionInfoSchema = TypeVar("DivisionInfoSchema", bound=DivisionInfoBaseSchema)
SeasonInfoSchema = TypeVar("SeasonInfoSchema", bound=SeasonInfoBaseSchema)
GameInfoSchema = TypeVar("GameInfoSchema", bound=GameInfoBaseSchema)
PlayerGameStatisticsInfoSchema = TypeVar("PlayerGameStatisticsInfoSchema", bound=PlayerGameStatisticsInfoBaseSchema)
FullStatisticsSchema = TypeVar("FullStatisticsSchema", bound=FullStatisticsBaseSchema)
