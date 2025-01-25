from pydantic import AnyHttpUrl, Field, field_validator

from common.domain.dto import BaseSchema


class MLBLTeamInfoResponseSchema(BaseSchema):
    team_id: int = Field(..., alias="TeamID")
    team_name: str = Field(..., alias="CompTeamNameRu")
    team_short_name: str = Field(..., alias="CompTeamShortNameRu")
    team_name_abc: str = Field(..., alias="CompTeamAbcNameRu")
    region: str = Field(..., alias="CompTeamRegionNameRu")


class MLBLPlayerInTeamResponseSchema(BaseSchema):
    player_id: int = Field(..., alias="PersonID")
    player_photo: AnyHttpUrl | None = Field(None, alias="PhotoUrl")
    player_number: int | None = Field(None, alias="PlayerNumber")

    @field_validator("player_number", mode="after")
    def set_player_number(cls, value: int) -> int | None:
        if value < 0:
            return None
        return value


class MLBLTeamResponseSchema(BaseSchema):
    team_info: MLBLTeamInfoResponseSchema = Field(..., alias="TeamName")
    players: list[MLBLPlayerInTeamResponseSchema] = Field(..., alias="Players")
