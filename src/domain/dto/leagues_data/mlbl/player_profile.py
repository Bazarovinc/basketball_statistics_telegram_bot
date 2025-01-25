from datetime import date, datetime

from pydantic import Field, field_validator, model_validator

from common.domain.dto.base import BaseSchema
from src.domain.dto.enums import MLBLGenderEnum, PositionEnum


class MLBLPlayerProfileResponseSchema(BaseSchema):
    person_id: int = Field(..., alias="PersonID")
    first_name: str = Field(..., alias="PersonFirstNameRu")
    last_name: str = Field(..., alias="PersonLastNameRu")
    middle_name: str = Field(..., alias="PersonSecondNameRu")
    gender: MLBLGenderEnum = Field(..., alias="PersonGender")
    birthdate: date = Field(..., alias="PersonBirth")
    height: int = Field(..., alias="PersonHeight")
    weight: int = Field(..., alias="PersonWeight")
    position: PositionEnum
    rank: str | None
    parsed_date: datetime = Field(default_factory=datetime.now)

    @field_validator("birthdate", mode="before")
    def parse_birthdate(cls, value: str | date) -> date:
        if isinstance(value, str):
            return datetime.strptime(value, "%d.%m.%Y").date()
        return value

    @model_validator(mode="before")
    def get(cls, values: dict) -> dict:
        _player_info = values.get("Players")[0]
        position = PositionEnum(int(_player_info.get("Position").get("PosID")))
        rank = _player_info.get("PersonRank").get("RankNameRu")
        rank = None if rank == "-" else rank
        values["position"] = position
        values["rank"] = rank
        return values
