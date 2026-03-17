import uuid
from datetime import datetime

from src.core.domain.dto import BaseSchema


class TeamDivisionBaseSchema(BaseSchema):
    """Схема таблицы team_division (composite PK: team_id, division_id)."""

    team_id: uuid.UUID
    division_id: uuid.UUID
    create_date: datetime
