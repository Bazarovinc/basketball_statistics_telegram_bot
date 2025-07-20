from pydantic import AnyHttpUrl, SecretStr
from pydantic_settings import BaseSettings


class TelegramSettings(BaseSettings):
    token: SecretStr = "7535981145:AAF5m2DP88YVeffat4cYkaGFPElWhCuXtPo"
    webhook: AnyHttpUrl = "https://bbae6hvom2ckgp3f1fob.containers.yandexcloud.net"
