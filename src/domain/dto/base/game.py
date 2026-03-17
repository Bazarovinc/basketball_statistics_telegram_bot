import json
import uuid
from datetime import datetime

from pydantic import Field, field_validator

from src.core.domain.dto import BaseSchema
from src.domain.enums import GameStatusEnum, GameQuarterEnum




class GameBaseSchema(BaseSchema):
    """Схема таблицы game."""

    game_id: uuid.UUID
    external_game_id: str
    division_id: uuid.UUID
    left_team_id: uuid.UUID | None = None
    right_team_id: uuid.UUID | None = None
    left_team_name: str
    right_team_name: str
    game_date: datetime | None = None
    left_team_points: int | None = Field(None, ge=0)
    right_team_points: int | None = Field(None, ge=0)
    left_team_quarters_points: dict[GameQuarterEnum, int] | None = Field(None)
    right_team_quarters_points: dict[GameQuarterEnum, int] | None = Field(None)
    game_status: GameStatusEnum
    game_place: str | None = None
    competition: str | None = None
    create_date: datetime
    last_update_date: datetime

    @field_validator("left_team_quarters_points", "right_team_quarters_points", mode="before")
    def validate_team_quarters_points(cls, value: str | dict) -> dict:
        if isinstance(value, str):
            return json.loads(value)
        return value
