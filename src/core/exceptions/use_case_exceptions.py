from src.core.exceptions.base import BaseCommonException


class PlayerProfileAlreadySavedError(BaseCommonException):
    message = "Такой игровой профиль уже сохранен"


class UserNotFoundError(BaseCommonException):
    message = "Пользователь еще не создан"


class UserAgreementNotFoundError(BaseCommonException):
    message = "Согласие пользователя не найдено"
