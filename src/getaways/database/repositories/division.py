import uuid

from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import DivisionBaseSchema
from src.domain.dto.leagues_data.base import DivisionInfoBaseSchema
from src.domain.interfaces.gateways.database.repositories.division_repository import IDivisionRepository
from src.utils import async_serialize


class DivisionRepository(BaseRepository, IDivisionRepository):
    table_name = "division"
    schema: type[DivisionBaseSchema]

    @async_serialize
    async def upsert(self, data: DivisionInfoBaseSchema, season_id: uuid.UUID) -> DivisionBaseSchema:
        row = await self._connection.fetchrow(
            """
            INSERT INTO division (division_id, external_division_id, name, league, season_id)
            VALUES ($1, $2, $3, $4::league_enum, $5)
            ON CONFLICT (external_division_id, league) DO NOTHING
            RETURNING division_id, external_division_id, name, league, create_date, season_id
            """,
            data.division_id,
            data.external_division_id,
            data.name,
            data.league,
            season_id,
        )
        if row is None:
            row = await self._connection.fetchrow(
                """
                SELECT division_id, external_division_id, name, league, create_date, season_id
                FROM division
                WHERE external_division_id = $1 AND league = $2::league_enum
                """,
                data.external_division_id,
                data.league,
            )
        return row
