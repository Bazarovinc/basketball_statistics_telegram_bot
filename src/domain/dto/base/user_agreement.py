import uuid
from datetime import datetime

from src.core.domain.dto import BaseSchema


class UserAgreementBaseSchema(BaseSchema):
    """Схема таблицы user_agreement."""

    user_id: uuid.UUID
    agreement_date: datetime
    message_id: int
