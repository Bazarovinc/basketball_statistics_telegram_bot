from pydantic import AnyHttpUrl, SecretStr
from pydantic_settings import BaseSettings


class TelegramSettings(BaseSettings):
    token: SecretStr
    webhook: AnyHttpUrl
