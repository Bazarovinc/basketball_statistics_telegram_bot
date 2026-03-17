from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import GameBaseSchema
from src.domain.dto.leagues_data.base import GameInfoBaseSchema
from src.domain.enums import GameQuarterEnum
from src.domain.interfaces.gateways.database.repositories.game_repository import IGameRepository
from src.utils import async_serialize


class GameRepository(BaseRepository, IGameRepository):
    table_name = "game"
    schema: type[GameBaseSchema]

    @async_serialize
    async def upsert(self, data: GameInfoBaseSchema) -> GameBaseSchema:
        row = await self._connection.fetchrow(
            """
            INSERT INTO game (
                game_id, external_game_id, division_id, left_team_id, right_team_id,
                left_team_name, right_team_name, game_date, left_team_points, right_team_points,
                left_team_quarters_points, right_team_quarters_points,
                game_status, game_place, competition
            )
            VALUES (
                $1, $2,
                COALESCE($3, (SELECT division_id FROM division WHERE external_division_id = $4 LIMIT 1)),
                COALESCE($5, (SELECT team_id FROM team WHERE external_team_id = $6 LIMIT 1)),
                COALESCE($7, (SELECT team_id FROM team WHERE external_team_id = $8 LIMIT 1)),
                $9, $10, $11, $12, $13, $14, $15, $16::game_status_enum, $17, $18
            )
            ON CONFLICT (game_id) DO UPDATE SET
                game_date = EXCLUDED.game_date,
                left_team_points = EXCLUDED.left_team_points,
                right_team_points = EXCLUDED.right_team_points,
                left_team_quarters_points = EXCLUDED.left_team_quarters_points,
                right_team_quarters_points = EXCLUDED.right_team_quarters_points,
                game_status = EXCLUDED.game_status,
                left_team_id = EXCLUDED.left_team_id,
                right_team_id = EXCLUDED.right_team_id,
                last_update_date = now()
            RETURNING game_id, external_game_id, division_id, left_team_id, right_team_id,
                left_team_name, right_team_name, game_date, left_team_points, right_team_points,
                left_team_quarters_points, right_team_quarters_points,
                game_status, game_place, competition, create_date, last_update_date
            """,
            data.game_id,
            data.external_game_id,
            data.division_id,
            data.external_division_id,
            data.left_team_id,
            data.external_left_team_id,
            data.right_team_id,
            data.external_right_team_id,
            data.left_team_name,
            data.right_team_name,
            data.game_date,
            data.left_team_points,
            data.right_team_points,
            data.left_team_quarters_points_serialized,
            data.right_team_quarters_points_serialized,
            data.game_status,
            data.game_place,
            data.competition,
        )
        return row
