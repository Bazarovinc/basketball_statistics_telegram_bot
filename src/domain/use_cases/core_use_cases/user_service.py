from src.domain.dto.input.user import UserInSchema
from src.domain.interfaces.gateways.database.unit_of_work import UserServiceBaseUnitOfWork


class UserService:
    def __init__(self, uow: UserServiceBaseUnitOfWork) -> None:
        self.uow = uow

    async def create_user(self, user: UserInSchema) -> None:
        async with self.uow:
            if not await self.uow.user_repo.is_exists(user.tg_id):
                await self.uow.user_repo.create(user)

    async def check_user_agreement_exists(self, tg_id: int) -> bool:
        async with self.uow:
            return await self.uow.user_agreement_repo.is_exists_by_tg_id(tg_id)

    async def add_user_agreement(self, user: UserInSchema, message_id: int) -> None:
        async with self.uow:
            if not await self.uow.user_repo.is_exists(user.tg_id):
                await self.uow.user_repo.create(user)
            await self.uow.user_agreement_repo.create(user.tg_id, message_id)

    async def delete_user(self, tg_id: int) -> None:
        async with self.uow:
            await self.uow.user_repo.delete(tg_id)
