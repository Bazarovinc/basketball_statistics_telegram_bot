from pydantic import Field
from pydantic_settings import BaseSettings

from src.settings.telegram import TelegramSettings


class AppSettings(BaseSettings):
    port: int = Field(default=8000)
    telegram: TelegramSettings = TelegramSettings()


app_settings = AppSettings()
