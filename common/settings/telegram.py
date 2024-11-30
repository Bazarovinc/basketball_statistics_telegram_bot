from pydantic import SecretStr
from pydantic_settings import BaseSettings


class TelegramSettings(BaseSettings):
    token: SecretStr
    admin_id: int
