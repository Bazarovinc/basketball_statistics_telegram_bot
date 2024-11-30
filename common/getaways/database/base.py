import uuid
from typing import Any, TypeAlias, TypeVar

from sqlalchemy import MetaData, Table
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Mapped

from common.utils.formatters import camel_to_snake

PK: TypeAlias = str | int | uuid.UUID


@as_declarative()
class Base:
    id: Mapped[PK]
    metadata: MetaData

    __table__: Table

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # Для корректной работы mypy
        pass

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return camel_to_snake(cls.__name__)

    __mapper_args__ = {"eager_defaults": True}


ModelType = TypeVar("ModelType", bound=Base)
