import uuid
from datetime import datetime

from pydantic import Field

from src.core.domain.dto import BaseSchema
from src.core.domain.dto.league_reader_input import LeagueTypeEnum


class DivisionBaseSchema(BaseSchema):
    """Схема таблицы division. В БД: UNIQUE (external_division_id, league)."""

    division_id: uuid.UUID
    external_division_id: str
    name: str = Field(..., min_length=3)
    league: LeagueTypeEnum
    create_date: datetime
    season_id: uuid.UUID
