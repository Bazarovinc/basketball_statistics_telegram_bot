from enum import Enum
from typing import TypeVar

from pydantic import AnyHttpUrl

from common.domain.dto.base import BaseSchema


class LeagueTypeEnum(Enum):
    MLBL = "МЛБЛ"
    ABL = "ABL"
    BCL = "ЛЧБ"


class LeagueReaderInputSchema(BaseSchema):
    league_type: LeagueTypeEnum
    player_url: AnyHttpUrl
    team_url: AnyHttpUrl | None = None
    player_id: int | str | None = None
    team_id: int | str | None = None


LeagueInputSchema = TypeVar("LeagueInputSchema", bound=LeagueReaderInputSchema)
