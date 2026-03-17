from pydantic import Field
from pydantic_settings import BaseSettings

from src.settings.object_storage import ObjectStorageSettings
from src.settings.postgres import PostgresSettings
from src.settings.telegram import TelegramSettings


class AppSettings(BaseSettings):
    port: int = Field(default=8000)
    telegram: TelegramSettings = TelegramSettings()
    postgres: PostgresSettings = PostgresSettings()
    object_storage: ObjectStorageSettings = ObjectStorageSettings()
