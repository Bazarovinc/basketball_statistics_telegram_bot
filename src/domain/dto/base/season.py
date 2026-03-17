import uuid
from datetime import datetime

from pydantic import Field, model_validator

from src.core.domain.dto import BaseSchema


class SeasonBaseSchema(BaseSchema):
    """Схема таблицы season (связь с лигами — таблица league_season)."""

    season_id: uuid.UUID
    name: str
    current_season: bool = Field(False)
    start_year: int = Field(..., ge=1900)
    end_year: int = Field(..., ge=1900)
    create_date: datetime
    last_update_date: datetime

    @model_validator(mode="after")
    def validate_end_year(self) -> "SeasonBaseSchema":
        if self.end_year < self.start_year:
            raise ValueError("end_year must be >= start_year")
        return self
