from pydantic import AnyHttpUrl

from src.core.domain.dto import BaseSchema
from src.core.domain.dto.league_reader_input import LeagueTypeEnum


class LeagueUrlsUserInputSchema(BaseSchema):
    player_url: AnyHttpUrl
    team_url: AnyHttpUrl | None = None
    league_type: LeagueTypeEnum
