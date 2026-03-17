import re
from collections import Counter
from datetime import date, datetime
from functools import cached_property
from typing import Self

from pydantic import AliasChoices, AliasPath, AnyHttpUrl, Field, field_validator, model_validator

from src.constants import SEASON_YEARS_COUNT
from src.core.domain.dto import BaseSchema
from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.dto.leagues_data.base import (
    DivisionInfoBaseSchema,
    GameInfoBaseSchema,
    PlayerGameStatisticsInfoBaseSchema,
    PlayerProfileInfoBaseSchema,
    SeasonInfoBaseSchema,
    TeamInfoBaseSchema,
)
from src.domain.dto.leagues_data.base.full_statistics import FullStatisticsBaseSchema, LeagueSeasonInfoBaseSchema
from src.domain.enums import GameStatusEnum, PositionEnum, GameQuarterEnum


class ABLPlayerProfileInfoSchema(PlayerProfileInfoBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.ABL
    profile_id: str = Field(..., validation_alias="id")
    player_id: int = Field(..., validation_alias="user_id", exclude=True)
    first_name: str = Field(..., validation_alias=AliasPath("user", "first_name"))
    last_name: str = Field(..., validation_alias=AliasPath("user", "last_name"))
    middle_name: str | None = Field(None, validation_alias=AliasPath("user", "middle_name"))
    player_height: int | None = Field(None, validation_alias=AliasPath("user", "profile", "height"))
    player_weight: int | None = Field(None, validation_alias=AliasPath("user", "profile", "weight"))
    birthdate: date | None = Field(None, validation_alias=AliasPath("user", "birth_date"))
    position: PositionEnum | None = Field(None, validation_alias=AliasPath("user", "basketball_profile", "position"))
    photo: str | None = Field(
        None, validation_alias=AliasChoices(AliasPath("user", "photo", "path"), AliasPath("photo", "path"))
    )
    photo_url: AnyHttpUrl | None = Field(
        None,
        validation_alias=AliasChoices(AliasPath("user", "photo", "path"), AliasPath("photo", "path")),
        exclude=True,
    )
    player_numbers: list[int] = Field(..., default_factory=list, exclude=True)

    @field_validator("profile_id", mode="before")
    def convert_external_id(cls, value: int) -> str:
        return str(value)

    @property
    def player_number_calculated(self) -> int | None:
        if not self.player_numbers:
            return None
        return Counter(self.player_numbers).most_common(1)[0][0]


class ABLTeamSeasonResponseSchema(BaseSchema):
    team_id: str = Field(..., validation_alias=AliasPath("tournament_team", "team", "id"))
    team_name: str = Field(..., validation_alias=AliasPath("tournament_team", "team", "name"))
    team_logo: AnyHttpUrl | None = Field(None, validation_alias=AliasPath("tournament_team", "team", "logo", "path"))
    division_id: str = Field(..., validation_alias=AliasPath("tournament_team", "tournament", "id"))
    division_name: str = Field(..., validation_alias=AliasPath("tournament_team", "tournament", "name"))
    season_id: str = Field(..., validation_alias=AliasPath("tournament_team", "tournament", "season", "id"))
    season_name: str = Field(..., validation_alias=AliasPath("tournament_team", "tournament", "season", "name"))

    @field_validator("team_id", "division_id", "season_id", mode="before")
    def convert_external_id(cls, value: int) -> str:
        return str(value)

    @cached_property
    def _season_years(self) -> tuple[int, int]:
        years = re.findall(r"\d{4}", self.season_name)
        if len(years) < SEASON_YEARS_COUNT:
            raise ValueError(f"Cannot parse season years from: {self.season_name!r}")
        return int(years[0]), int(years[1])

    @property
    def season_start_year(self) -> int:
        return self._season_years[0]

    @property
    def season_end_year(self) -> int:
        return self._season_years[1]


class ABLTeamInfoSchema(TeamInfoBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.ABL


class ABLDivisionInfoSchema(DivisionInfoBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.ABL
    teams: list[ABLTeamInfoSchema]


class ABLLeagueSeasonInfoSchema(LeagueSeasonInfoBaseSchema):
    external_season_id: str
    name: str
    league: LeagueTypeEnum = LeagueTypeEnum.ABL


class ABLSeasonInfoSchema(SeasonInfoBaseSchema):
    divisions: list[ABLDivisionInfoSchema]
    league_seasons: list[ABLLeagueSeasonInfoSchema] = Field(..., max_length=1, min_length=1)


class ABLPlayerGameStatisticsInfoSchema(PlayerGameStatisticsInfoBaseSchema):
    is_start: bool | None = None
    played_time_seconds: int | None = Field(None, validation_alias="played_time")


class ABLGameInfoSchema(GameInfoBaseSchema):
    id: int = Field(..., validation_alias="id", exclude=True)
    external_game_id: str = Field(..., validation_alias="id")
    external_left_team_id: str = Field(..., validation_alias=AliasPath("competitor_team", "id"))
    left_team_name: str = Field(..., validation_alias=AliasPath("competitor_team", "name"))
    left_team_points: int | None = Field(0, validation_alias="competitor_team_score")
    right_team_name: str = Field(..., validation_alias=AliasPath("team", "name"))
    external_right_team_id: str = Field(..., validation_alias=AliasPath("team", "id"))
    right_team_points: int | None = Field(0, validation_alias="team_score")
    game_date: datetime | None = Field(None, validation_alias="datetime")
    game_place: str | None = Field(None, validation_alias="location")
    score_by_period: dict[int, list[int]] | None = Field(None, exclude=True)
    external_division_id: str = Field(..., validation_alias=AliasPath("tournament", "id"))
    game_status: GameStatusEnum = GameStatusEnum.finished
    player_statistics: ABLPlayerGameStatisticsInfoSchema | None = None

    @field_validator(
        "external_game_id", "external_left_team_id", "external_right_team_id", "external_division_id", mode="before"
    )
    def convert_external_id(cls, value: int) -> str:
        return str(value)

    @model_validator(mode="after")
    def set_teams_quarters_points(self) -> Self:
        if self.score_by_period:
            quarters = sorted(self.score_by_period.keys())
            for quarter, quarter_enum_value in zip(quarters, GameQuarterEnum):
                teams_score: list[int] = self.score_by_period.get(quarter)
                self.left_team_quarters_points[quarter_enum_value] = teams_score[0]
                self.right_team_quarters_points[quarter_enum_value] = teams_score[1]
        return self


class ABLFullStatisticsSchema(FullStatisticsBaseSchema):
    player_profile: ABLPlayerProfileInfoSchema
    seasons: list[ABLSeasonInfoSchema]
    games: list[ABLGameInfoSchema]
