import uuid

from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import PlayerTeamBaseSchema
from src.domain.interfaces.gateways.database.repositories.player_team_repository import IPlayerTeamRepository


class PlayerTeamRepository(BaseRepository, IPlayerTeamRepository):
    table_name = "player_team"
    schema: type[PlayerTeamBaseSchema]

    async def upsert(self, player_profile_id: uuid.UUID, team_id: uuid.UUID) -> None:
        await self._connection.execute(
            """
            INSERT INTO player_team (player_profile_id, team_id)
            VALUES ($1, $2)
            ON CONFLICT (player_profile_id, team_id) DO NOTHING
            """,
            player_profile_id,
            team_id,
        )
