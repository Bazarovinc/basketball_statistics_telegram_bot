"""
Окружение для миграций Alembic.

Миграции выполняются через синхронный движок (psycopg2).
Приложение использует чистый asyncpg — SQLAlchemy нужен только для запуска миграций.

Настройки БД читаются из переменных окружения (без загрузки AppSettings),
чтобы команды alembic работали без TELEGRAM_TOKEN и TELEGRAM_WEBHOOK.

Переменные: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB
Либо задайте DATABASE_URL напрямую для postgresql+psycopg2.
"""

import os
from logging.config import fileConfig
from urllib.parse import quote_plus

from alembic import context
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.pool import NullPool

# Загрузка .env при наличии python-dotenv (опционально)
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# объект конфигурации Alembic
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Без MetaData: автогенерация по моделям не используется (проект на asyncpg).
target_metadata = None


def _get_sync_url() -> str:
    """URL для синхронного подключения к PostgreSQL (только для миграций)."""
    url = os.getenv("DATABASE_URL")
    if url:
        if url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
        elif url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+psycopg2://", 1)
        return url

    user = os.getenv("POSTGRES_USER", "ctelma")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "baskteball_statistics_telegram_bot")

    password_encoded = quote_plus(password)
    return f"postgresql+psycopg2://{user}:{password_encoded}@{host}:{port}/{db}"


def run_migrations_offline() -> None:
    """Запуск миграций в offline-режиме (только генерация SQL)."""
    url = _get_sync_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запуск миграций в online-режиме (реальное подключение к БД)."""
    url = _get_sync_url()
    connectable = create_engine(url, poolclass=NullPool)

    with connectable.connect() as connection:
        do_run_migrations(connection)


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
