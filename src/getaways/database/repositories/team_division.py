import uuid

from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import TeamDivisionBaseSchema
from src.domain.interfaces.gateways.database.repositories.team_division_repository import ITeamDivisionRepository


class TeamDivisionRepository(BaseRepository, ITeamDivisionRepository):
    table_name = "team_division"
    schema: type[TeamDivisionBaseSchema]

    async def upsert(self, team_id: uuid.UUID, division_id: uuid.UUID) -> None:
        await self._connection.fetchrow(
            """
            INSERT INTO team_division (team_id, division_id)
            VALUES ($1, $2)
            ON CONFLICT (team_id, division_id) DO NOTHING
            """,
            team_id,
            division_id,
        )
