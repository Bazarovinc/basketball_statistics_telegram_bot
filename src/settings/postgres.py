from pydantic_settings import SettingsConfigDict

from src.core.settings import PostgresBaseSettings


class PostgresSettings(PostgresBaseSettings):
    db: str = "baskteball_statistics_telegram_bot"
    user: str = "ctelma"
    model_config = SettingsConfigDict(env_prefix="POSTGRES_")
