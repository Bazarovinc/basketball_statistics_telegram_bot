from uuid import UUID

from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import UserAgreementBaseSchema
from src.domain.interfaces.gateways.database.repositories.user_agreement_repository import (
    IUserAgreementRepository,
)


class UserAgreementRepository(BaseRepository, IUserAgreementRepository):
    table_name = "user_agreement"
    schema: type[UserAgreementBaseSchema]

    async def is_exists_by_tg_id(self, tg_id: int) -> bool:
        row = await self._connection.fetchrow(
            """
            SELECT EXISTS(
                SELECT 1 FROM user_agreement ua
                JOIN "user" u ON ua.user_id = u.user_id
                WHERE u.tg_id = $1
            ) AS "exists"
            """,
            tg_id,
        )
        return row["exists"] if row else False

    async def is_exists_by_user_id(self, user_id: UUID) -> bool:
        row = await self._connection.fetchrow(
            'SELECT EXISTS(SELECT 1 FROM user_agreement WHERE user_id = $1) AS "exists"',
            user_id,
        )
        return row["exists"] if row else False

    async def create(self, tg_id: int, message_id: int) -> None:
        await self._connection.execute(
            """
            INSERT INTO user_agreement (user_id, message_id)
            SELECT user_id, $2 FROM "user" WHERE tg_id = $1
            """,
            tg_id,
            message_id,
        )
