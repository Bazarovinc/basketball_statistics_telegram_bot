from functools import cached_property

from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    filename: str = "bb_stats_db"
    pool_size: int = 10
    pool_overflow_size: int = 10
    pool_pre_ping: bool = True
    echo: bool = False
    autoflush: bool = False
    autocommit: bool = False
    expire_on_commit: bool = False

    @cached_property
    def dsn(self) -> str:
        return f"sqlite+aiosqlite:///{self.filename}"
