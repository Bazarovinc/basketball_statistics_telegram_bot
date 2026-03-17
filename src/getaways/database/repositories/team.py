from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import TeamBaseSchema
from src.domain.dto.leagues_data.base import TeamInfoBaseSchema
from src.domain.interfaces.gateways.database.repositories.team_repository import ITeamRepository
from src.utils import async_serialize


class TeamRepository(BaseRepository, ITeamRepository):
    table_name = "team"
    schema: type[TeamBaseSchema]

    @async_serialize
    async def upsert(self, data: TeamInfoBaseSchema) -> TeamBaseSchema:
        logo_value = str(data.logo) if data.logo is not None else None
        row = await self._connection.fetchrow(
            """
            INSERT INTO team (
                team_id,external_team_id, team_name, team_short_name, team_name_abc, region, logo, league
                )
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8::league_enum)
            ON CONFLICT (external_team_id, league) DO UPDATE SET
                team_name = EXCLUDED.team_name,
                team_short_name = EXCLUDED.team_short_name,
                team_name_abc = EXCLUDED.team_name_abc,
                region = EXCLUDED.region,
                logo = EXCLUDED.logo
            RETURNING
                team_id,
                external_team_id,
                team_name,
                team_short_name,
                team_name_abc,
                region,
                logo,
                league,
                create_date
            """,
            data.team_id,
            data.external_team_id,
            data.team_name,
            data.team_short_name,
            data.team_name_abc,
            data.region,
            logo_value,
            data.league,
        )
        return row
