from abc import ABC, abstractmethod

from src.domain.dto.input.user import UserInSchema


class IUserRepository(ABC):
    @abstractmethod
    async def create(self, data: UserInSchema) -> None:
        raise NotImplementedError

    @abstractmethod
    async def is_exists(self, tg_id: int) -> bool:
        raise NotImplementedError
