import uuid
from datetime import date, datetime

from pydantic import Field

from src.core.domain.dto import BaseSchema
from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.enums import PositionEnum


class PlayerProfileBaseSchema(BaseSchema):
    """Схема таблицы player_profile."""

    player_profile_id: uuid.UUID
    user_id: uuid.UUID
    profile_id: str
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    middle_name: str | None = Field(None, min_length=3)
    player_height: int | None = Field(None, gt=0)
    player_weight: int | None = Field(None, gt=0)
    birthdate: date | None = None
    position: PositionEnum | None = None
    player_rank: int | None = None
    photo: str | None = None
    player_number: int | None = Field(None, ge=0, lt=100)
    league: LeagueTypeEnum | None = None
    parse_date: datetime
    create_date: datetime
    last_update_date: datetime
