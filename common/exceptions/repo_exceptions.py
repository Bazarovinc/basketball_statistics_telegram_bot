from common.exceptions.base import BaseCommonException


class NotFoundException(BaseCommonException):
    message = "Запись в БД не найдена"


class NoFieldException(BaseCommonException):
    message = "У таблицы {model} нет такого поля '{field}'"

    def __init__(self, model: str, field: str) -> None:
        self.message = self.message.format(model=model, field=field)
        super().__init__()
