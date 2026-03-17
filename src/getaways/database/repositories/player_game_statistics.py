from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import PlayerGameStatisticsBaseSchema
from src.domain.dto.leagues_data.base import PlayerGameStatisticsInfoBaseSchema
from src.domain.interfaces.gateways.database.repositories.player_game_statistics_repository import (
    IPlayerGameStatisticsRepository,
)


class PlayerGameStatisticsRepository(BaseRepository, IPlayerGameStatisticsRepository):
    table_name = "player_game_statistics"
    schema: type[PlayerGameStatisticsBaseSchema]

    async def upsert(self, data: PlayerGameStatisticsInfoBaseSchema) -> None:
        await self._connection.execute(
            """
            INSERT INTO player_game_statistics (
                player_game_statistics_id, player_profile_id, game_id,
                total_points, points_1, shots_1, points_2, shots_2, points_3, shots_3,
                assists, blocks, defence_rebounds, offence_rebounds, steals, turnovers,
                fouls, opponent_fouls, played_time_seconds, plus_minus, is_start, kpi, player_number
            )
            VALUES (
                $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23
            )
            ON CONFLICT (player_profile_id, game_id) DO UPDATE SET
                total_points = EXCLUDED.total_points,
                points_1 = EXCLUDED.points_1,
                shots_1 = EXCLUDED.shots_1,
                points_2 = EXCLUDED.points_2,
                shots_2 = EXCLUDED.shots_2,
                points_3 = EXCLUDED.points_3,
                shots_3 = EXCLUDED.shots_3,
                assists = EXCLUDED.assists,
                blocks = EXCLUDED.blocks,
                defence_rebounds = EXCLUDED.defence_rebounds,
                offence_rebounds = EXCLUDED.offence_rebounds,
                steals = EXCLUDED.steals,
                turnovers = EXCLUDED.turnovers,
                fouls = EXCLUDED.fouls,
                opponent_fouls = EXCLUDED.opponent_fouls,
                played_time_seconds = EXCLUDED.played_time_seconds,
                plus_minus = EXCLUDED.plus_minus,
                is_start = EXCLUDED.is_start,
                kpi = EXCLUDED.kpi
            """,
            data.player_game_statistics_id,
            data.player_profile_id,
            data.game_id,
            data.total_points,
            data.points_1,
            data.shots_1,
            data.points_2,
            data.shots_2,
            data.points_3,
            data.shots_3,
            data.assists,
            data.blocks,
            data.defence_rebounds,
            data.offence_rebounds,
            data.steals,
            data.turnovers,
            data.fouls,
            data.opponent_fouls,
            data.played_time_seconds,
            data.plus_minus,
            data.is_start,
            data.kpi,
            data.player_number,
        )
