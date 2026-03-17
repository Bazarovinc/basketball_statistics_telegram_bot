from dataclasses import dataclass

from pydantic import Field

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


class BCLPlayerProfileInfoSchema(PlayerProfileInfoBaseSchema):
    photo: str | None = None
    league: LeagueTypeEnum = LeagueTypeEnum.BCL


class BCLTeamSeasonResponseSchema(BaseSchema):
    pass


class BCLTeamInfoSchema(TeamInfoBaseSchema):
    region: str = "Москва"
    league: LeagueTypeEnum = LeagueTypeEnum.BCL


class BCLDivisionInfoSchema(DivisionInfoBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.BCL
    teams: list[BCLTeamInfoSchema]


class BCLLeagueSeasonInfoSchema(LeagueSeasonInfoBaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.BCL


class BCLSeasonInfoSchema(SeasonInfoBaseSchema):
    league_seasons: list[BCLLeagueSeasonInfoSchema] = Field(..., min_length=1, max_length=2)


class BCLPlayerGameStatisticsInfoSchema(PlayerGameStatisticsInfoBaseSchema):
    pass


class BCLGameInfoSchema(GameInfoBaseSchema):
    pass


class BCLFullStatisticsSchema(FullStatisticsBaseSchema):
    pass


@dataclass
class BCLPlayerSeasonSchema:
    season_id: int
    team_id: int
    season_name: str
