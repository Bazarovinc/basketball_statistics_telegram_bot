import uuid

from pydantic import UUID4, Field

from src.core.domain.dto import BaseSchema


class UserInSchema(BaseSchema):
    user_id: UUID4 = Field(..., default_factory=uuid.uuid4)
    tg_id: int
    tg_username: str | None = Field(None, max_length=40)
