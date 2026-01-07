from pydantic import AnyHttpUrl, Field, SecretStr
from pydantic_settings import BaseSettings


class TelegramSettings(BaseSettings):
    token: SecretStr = Field(..., description="Телеграм токен бота")
    webhook: AnyHttpUrl = Field(..., description="Вебхук, в который ходит телеграм")
