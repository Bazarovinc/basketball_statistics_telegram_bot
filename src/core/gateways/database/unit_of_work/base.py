from typing import TYPE_CHECKING

import asyncpg

from src.core.gateways.database.repositories.base_repository import BaseRepository

if TYPE_CHECKING:
    from asyncpg.transaction import Transaction


class BaseUnitOfWork:
    """Unit of work на asyncpg: одна транзакция на соединении из пула."""

    def __init__(self, pool: asyncpg.Pool) -> None:
        self._pool = pool
        self._conn: asyncpg.Connection | None = None
        self._transaction: Transaction | None = None
        self._repo_map = {
            attr_name: attr_type
            for attr_name, attr_type in getattr(self.__class__, "__annotations__", {}).items()
            if isinstance(attr_type, type) and issubclass(attr_type, BaseRepository)
        }

    async def __aenter__(self) -> "BaseUnitOfWork":
        self._conn = await self._pool.acquire()
        self._transaction = self._conn.transaction()
        await self._transaction.start()
        for attr_name, attr_type in self._repo_map.items():
            setattr(self, attr_name, attr_type(connection=self._conn))
        return self

    async def __aexit__(self, exc_type: type, exc_val: BaseException, exc_tb: object) -> None:
        try:
            if exc_type is not None:
                await self._transaction.rollback()
            else:
                await self._transaction.commit()
        finally:
            if self._conn is not None:
                await self._pool.release(self._conn)
            self._transaction = None
            self._conn = None
            for attr_name in list(self._repo_map.keys()):
                if hasattr(self, attr_name):
                    delattr(self, attr_name)
