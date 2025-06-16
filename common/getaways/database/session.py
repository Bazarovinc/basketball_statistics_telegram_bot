from asyncio import current_task

from sqlalchemy.ext.asyncio import async_scoped_session, async_sessionmaker, create_async_engine  # AsyncSession,

from common.settings.database import DatabaseSettings

# from contextlib import asynccontextmanager
# from typing import AsyncGenerator, cast


class SessionManager:
    def __init__(self, settings: DatabaseSettings) -> None:
        self.settings = settings
        _engine = create_async_engine(
            self.settings.dsn,
            pool_pre_ping=self.settings.pool_pre_ping,
            echo=self.settings.echo,
        )
        self._session_local = async_sessionmaker(
            autocommit=self.settings.autocommit,
            autoflush=self.settings.autoflush,
            bind=_engine,
        )
        self._scoped_session = async_scoped_session(self._session_local, scopefunc=current_task)


# TODO: реализовать генерацию сессий
