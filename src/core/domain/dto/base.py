from typing import TypeVar

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


Schema = TypeVar("Schema", bound=BaseSchema)
