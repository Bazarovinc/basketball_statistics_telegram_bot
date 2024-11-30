from collections.abc import Sequence
from typing import Type

import sqlalchemy as sa
from gr_nrt_common.geteaways.database.base import ModelType
from gr_nrt_common.geteaways.database.repositories.base_repository import BaseRepository
from gr_nrt_common.geteaways.database.repositories.interfaces import (
    ICreateUpdateMixin,
    IDeleteMixin,
    IDType,
    IRetrieveManyMixin,
    IRetrieveOneMixin,
)
from pydantic import TypeAdapter
from sqlalchemy import exc

from common.domain.dto.base import Schema
from common.exceptions.repo_exceptions import NoFieldException, NotFoundException


class CreateUpdateMixin(ICreateUpdateMixin, BaseRepository):
    async def create(self, data: dict) -> Schema:
        obj = self.model(**data)
        self._session.add(obj)
        await self._session.flush()
        return TypeAdapter(self.schema).validate_python(obj)

    async def update(self, id: IDType, data: dict) -> None:
        _query = sa.update(self.model).where(self.model.id == id).values(**data)
        await self._session.execute(_query)
        await self._session.flush()


class RetrieveOneMixin(IRetrieveOneMixin, BaseRepository):
    async def _get_one_by_query(self, query: sa.Select) -> ModelType:
        result = await self._session.execute(query)
        try:
            return result.unique().scalars().one()
        except exc.NoResultFound:
            raise NotFoundException

    async def _get_first_by_query(self, query: sa.Select) -> ModelType | None:
        result = await self._session.execute(query)
        return result.unique().scalars().first()

    def _filter(self, filters: dict) -> sa.Select:
        _query = sa.select(self.model)
        for field, value in filters.items():
            try:
                attribute = getattr(self.model, field)
            except AttributeError:
                raise NoFieldException(self.model.__name__, field)
            if isinstance(value, Sequence) and not isinstance(value, str):
                _query = _query.where(attribute.in_(value))
            else:
                _query = _query.where(attribute == value)
        return _query

    async def get_one_by_id(self, id: IDType, response_schema: Type[Schema] = None) -> Schema:
        _query = sa.select(self.model).where(self.model.id == id)
        _obj = await self._get_one_by_query(_query)
        return TypeAdapter(response_schema or self.schema).validate_python(_obj)

    async def get_one_by_filters(
        self, filters: dict, response_schema: Type[Schema] = None
    ) -> Schema:
        _obj = await self._get_one_by_query(self._filter(filters))
        return TypeAdapter(response_schema or self.schema).validate_python(_obj)

    async def get_first_by_filters(
        self, filters: dict, response_schema: Schema = None
    ) -> Schema | None:
        if _obj := await self._get_first_by_query(self._filter(filters)):
            return TypeAdapter(response_schema or self.schema).validate_python(_obj)
        return None


class RetrieveManyMixin(IRetrieveManyMixin, BaseRepository):
    async def get_many(self, filters: dict, response_schema: Type[Schema] = None) -> list[Schema]:
        _query = sa.select(self.model)
        for field, value in filters.items():
            try:
                attribute = getattr(self.model, field)
            except AttributeError:
                raise NoFieldException(self.model.__name__, field)
            if isinstance(value, Sequence) and not isinstance(value, str):
                _query = _query.where(attribute.in_(value))
            else:
                _query = _query.where(attribute == value)
        result = await self._session.execute(_query)
        _objs = result.unique().scalars().all()
        return TypeAdapter(
            list[response_schema] if response_schema else list[self.schema]
        ).validate_python(_objs)


class DeleteMixin(IDeleteMixin, BaseRepository):
    async def delete(self, id: IDType) -> None:
        _query = sa.delete(self.model).where(self.model.id == id)
        result = await self._session.execute(_query)
        if result.rowcount == 0:
            raise NotFoundException
        await self._session.flush()
