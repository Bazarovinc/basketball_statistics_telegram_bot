from typing import Self

from pydantic import model_validator

from src.constants import BCL_HOST
from src.core.domain.dto.league_reader_input import LeagueReaderInputSchema, LeagueTypeEnum


class BCLInputBaseSchema(LeagueReaderInputSchema):
    league_type: LeagueTypeEnum = LeagueTypeEnum.BCL
    _host: str = BCL_HOST
    # пока не буду парсить из урла ничего, т.к. в него надо будет просто сходить

    @model_validator(mode="after")
    def set_player_id(self) -> Self:
        self.player_id = self.player_url.path.split("/")[-1]
        return self
