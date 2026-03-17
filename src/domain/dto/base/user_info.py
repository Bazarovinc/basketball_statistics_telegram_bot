import uuid
from datetime import date, datetime

from pydantic import Field

from src.core.domain.dto import BaseSchema
from src.domain.enums import GenderEnum, PositionEnum


class UserInfoBaseSchema(BaseSchema):
    """Схема таблицы user_info (gender_enum в БД: 'male', 'female')."""

    user_id: uuid.UUID
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    middle_name: str | None = Field(None, min_length=3)
    gender: GenderEnum
    birthdate: date
    height: int = Field(..., gt=0)
    weight: int = Field(..., gt=0)
    position: PositionEnum
    photo: str | None = None
    last_update_date: datetime
