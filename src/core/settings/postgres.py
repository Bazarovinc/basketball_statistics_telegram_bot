from typing import Literal

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class PostgresBaseSettings(BaseSettings):
    """
    Класс базовых конфигураций PostgreSQL

    Attributes:
        scheme: схема подключения ('postgresql+asyncpg' для асинхронного или 'postgresql' для синхронного)
        host: хост базы данных
        port: порт базы данных
        user: пользователь базы данных
        password: пароль пользователя (хранится в SecretStr)
        db: название базы данных
        pool_size: размер пула соединений
        pool_overflow_size: максимальный размер переполнения пула
        pool_pre_ping: проверка соединения перед использованием
        echo: логирование SQL запросов
        autoflush: автоматический сброс сессии
        autocommit: автоматическое подтверждение транзакций
        expire_on_commit: сброс состояния объектов после коммита
        local: флаг локального подключения (для разработки)
    """

    scheme: Literal["postgresql+asyncpg", "postgresql"] = "postgresql"
    host: str = "localhost"
    port: str = "5432"
    user: str = "postgres"
    password: SecretStr = Field(default=SecretStr("postgres"))
    db: str = "postgres"
    pool_size: int = 10
    pool_overflow_size: int = 15
    pool_pre_ping: bool = True
    echo: bool = False
    autoflush: bool = False
    autocommit: bool = False
    expire_on_commit: bool = False
    local: bool = False

    @property
    def dsn(self) -> str:
        """
        Формирует строку подключения (DSN) к PostgreSQL для SQLAlchemy.

        Returns:
            строка подключения в формате: 'scheme://user:password@host:port/db'
        """
        return f"{self.scheme}://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.db}"
