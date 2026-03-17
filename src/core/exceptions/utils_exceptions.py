from src.core.exceptions.base import BaseCommonException


class SerializationException(BaseCommonException):
    message: str = (
        "Вероятная ошибка, что не была указана конфигурация"
        " model_config = ConfigDict(from_attributes=True)."
        " Ошибка: {exception}"
    )

    def __init__(self, exception: Exception) -> None:
        self.message = self.message.format(exception=exception)
        super().__init__()
