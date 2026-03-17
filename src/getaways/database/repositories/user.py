from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import UserBaseSchema
from src.domain.dto.input.user import UserInSchema
from src.domain.interfaces.gateways.database.repositories import IUserRepository


class UserRepository(BaseRepository, IUserRepository):
    table_name = "user"
    schema: type[UserBaseSchema]

    async def create(self, data: UserInSchema) -> None:
        await self._connection.execute(
            """
            INSERT INTO "user" (user_id, tg_id, tg_username)
            VALUES ($1, $2, $3)
            ON CONFLICT (tg_id) DO NOTHING;
            """,
            data.user_id,
            data.tg_id,
            data.tg_username,
        )

    async def get_user_by_tg_id(self, tg_id: int) -> UserBaseSchema | None:
        row = await self._connection.fetchrow(
            'SELECT user_id, tg_id, tg_username, registration_date FROM "user" WHERE tg_id = $1',
            tg_id,
        )
        if row is None:
            return None
        return UserBaseSchema(
            user_id=row["user_id"],
            tg_id=row["tg_id"],
            tg_username=row["tg_username"],
            registration_date=row["registration_date"],
        )

    async def is_exists(self, tg_id: int) -> bool:
        row = await self._connection.fetchrow(
            'SELECT EXISTS(SELECT 1 FROM "user" WHERE tg_id = $1) AS "exists"',
            tg_id,
        )
        return row["exists"] if row else False

    async def delete(self, tg_id: int) -> None:
        await self._connection.execute('DELETE FROM "user" WHERE tg_id = $1', tg_id)
