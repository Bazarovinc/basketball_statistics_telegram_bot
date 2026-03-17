from datetime import datetime

from pydantic import UUID4, Field

from src.core.domain.dto import BaseSchema


class UserBaseSchema(BaseSchema):
    """Схема таблицы user."""

    user_id: UUID4
    tg_id: int
    tg_username: str = Field(..., min_length=3, max_length=40)
    registration_date: datetime
