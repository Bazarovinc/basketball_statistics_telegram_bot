from common.exceptions.base import BaseCommonException


class URLValidationException(BaseCommonException):
    message = "Ошибка валидации URL полученного от пользователя"


class ServerNotAvailableException(BaseCommonException):
    message = "Сервер лиги не отвечает"
