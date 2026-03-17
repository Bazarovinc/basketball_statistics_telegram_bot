from abc import ABC, abstractmethod

from src.domain.dto.base import UserBaseSchema
from src.domain.dto.input.user import UserInSchema


class IUserRepository(ABC):
    @abstractmethod
    async def create(self, data: UserInSchema) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_tg_id(self, tg_id: int) -> UserBaseSchema | None:
        """Возвращает пользователя по tg_id или None."""
        raise NotImplementedError

    @abstractmethod
    async def is_exists(self, tg_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, tg_id: int) -> None:
        raise NotImplementedError
