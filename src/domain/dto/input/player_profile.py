from datetime import date

from common.domain.dto import BaseSchema
from src.domain.dto.enums import PlayerGenderEnum, PositionEnum


class MLBLPlayerProfileResponseSchema(BaseSchema):
    person_id: int
    first_name: str
    last_name: str
    middle_name: str
    gender: PlayerGenderEnum
    birthdate: date
    height: int
    weight: int
    position: PositionEnum
    player_rank: str | None = None
    photo: str | None = None
    player_number: int | None = None
