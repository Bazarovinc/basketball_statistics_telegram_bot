from abc import ABC, abstractmethod
from typing import TypeAlias
from uuid import UUID

from common.domain.dto import Schema

IDType: TypeAlias = int | UUID | str


class BaseRepositoryProtocol(ABC):
    pass


class ICreateUpdateMixin(BaseRepositoryProtocol):
    @abstractmethod
    async def create(self, data: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: IDType, data: dict) -> None:
        raise NotImplementedError


class IRetrieveOneMixin(BaseRepositoryProtocol):
    @abstractmethod
    async def get_one_by_id(self, id: IDType, response_schema: Schema = None) -> Schema:
        raise NotImplementedError

    @abstractmethod
    async def get_one_by_filters(self, filters: dict, response_schema: Schema = None) -> Schema:
        raise NotImplementedError

    @abstractmethod
    async def get_first_by_filters(
        self, filters: dict, response_schema: Schema = None
    ) -> Schema | None:
        raise NotImplementedError


class IRetrieveManyMixin(BaseRepositoryProtocol):
    @abstractmethod
    async def get_many(self, filters: dict, response_schema: Schema = None) -> list[Schema]:
        raise NotImplementedError


class IDeleteMixin(BaseRepositoryProtocol):
    @abstractmethod
    async def delete(self, id: IDType) -> None:
        raise NotImplementedError


class RepositoryInterface(ICreateUpdateMixin, IRetrieveOneMixin, IRetrieveManyMixin, IDeleteMixin):
    pass
