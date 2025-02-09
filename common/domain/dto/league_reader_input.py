from enum import Enum
from typing import TypeVar

from pydantic import AnyHttpUrl, model_validator

from common.domain.dto.base import BaseSchema


class LeagueTypeEnum(Enum):
    MLBL = "МЛБЛ"
    ABL = "ABL"
    BCL = "ЛЧБ"


class LeagueReaderInputSchema(BaseSchema):
    _host: str
    league_type: LeagueTypeEnum
    player_url: AnyHttpUrl
    team_url: AnyHttpUrl | None = None
    player_id: int | str | None = None
    team_id: int | str | None = None

    @model_validator(mode="after")
    def validate_league(self) -> "LeagueReaderInputSchema":
        if self._host not in self.player_url.host:
            raise ValueError("Хост player_url не совпадает с хостом лиги")
        return self


LeagueInputSchema = TypeVar("LeagueInputSchema", bound=LeagueReaderInputSchema)
