import asyncpg

from src.core.settings.postgres import PostgresBaseSettings


async def get_pool(postgres_settings: PostgresBaseSettings) -> asyncpg.Pool:
    """Создаёт пул соединений asyncpg."""
    return await asyncpg.create_pool(
        dsn=postgres_settings.dsn,
        min_size=1,
        max_size=postgres_settings.pool_size,
        command_timeout=60,
    )
