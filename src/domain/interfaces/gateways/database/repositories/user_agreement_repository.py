import uuid
from abc import ABC, abstractmethod


class IUserAgreementRepository(ABC):
    @abstractmethod
    async def is_exists_by_tg_id(self, tg_id: int) -> bool:
        """Проверяет наличие согласия пользователя по tg_id."""
        raise NotImplementedError

    @abstractmethod
    async def is_exists_by_user_id(self, user_id: uuid.UUID) -> bool:
        """Проверяет наличие согласия пользователя по user_id."""
        raise NotImplementedError

    @abstractmethod
    async def create(self, tg_id: int, message_id: int) -> None:
        """Создаёт запись о согласии пользователя по tg_id и message_id."""
        raise NotImplementedError
