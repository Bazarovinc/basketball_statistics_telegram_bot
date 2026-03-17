from src.core.exceptions.base import BaseCommonException


class NotFoundException(BaseCommonException):
    message = "Запись в БД не найдена"


class NoFieldException(BaseCommonException):
    message = "For model {model} no such field '{field}'"

    def __init__(self, model: str, field: str) -> None:
        self.message = self.message.format(model=model, field=field)
        super().__init__()


class DuplicatedRecordException(BaseCommonException):
    message = "Такая запись уже существует"


class InvalidIdentifierException(BaseCommonException):
    """Недопустимое имя таблицы/колонки для подстановки в SQL (риск SQL-инъекции)."""

    def __init__(self, name: str) -> None:
        self.name = name
