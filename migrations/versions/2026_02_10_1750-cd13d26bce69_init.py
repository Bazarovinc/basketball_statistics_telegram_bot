"""init

Revision ID: cd13d26bce69
Revises:
Create Date: 2026-02-10 17:50:48.547113

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "cd13d26bce69"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE TYPE league_enum AS ENUM ('МЛБЛ', 'ABL', 'ЛЧБ');")
    op.execute("""
        CREATE TABLE IF NOT EXISTS "user" (
            user_id uuid NOT NULL UNIQUE,
            tg_id bigint NOT NULL UNIQUE,
            tg_username text NOT NULL check ( length(tg_username) <=40 and length(tg_username) >= 3),
            registration_date timestamp with time zone NOT NULL default now(),
            PRIMARY KEY (user_id)
        );
    """)
    op.execute('CREATE INDEX IF NOT EXISTS ix_user_tg_id ON "user" (tg_id);')

    op.execute("CREATE TYPE gender_enum AS ENUM ('male', 'female');")

    op.execute("""
        CREATE TABLE IF NOT EXISTS user_info (
            user_id uuid NOT NULL UNIQUE references "user"(user_id) ON DELETE CASCADE,
            first_name text not null check (length(first_name) >= 3),
            last_name text not null check (length(last_name) >= 3),
            middle_name text check (middle_name is null or length(middle_name) >= 3),
            gender gender_enum not null,
            birthdate date not null,
            height smallint not null check (height > 0 ),
            weight smallint not null check (weight > 0 ),
            position smallint not null check(position >= 1 and position <= 5),
            photo text,
            last_update_date timestamp with time zone NOT NULL default now(),
            PRIMARY KEY (user_id)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS user_agreement (
            user_id uuid NOT NULL UNIQUE references "user"(user_id) ON DELETE CASCADE,
            agreement_date timestamp with time zone NOT NULL default now(),
            message_id bigint NOT NULL,
            PRIMARY KEY (user_id)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS season (
            season_id uuid NOT NULL UNIQUE,
            name text NOT NULL,
            current_season boolean NOT NULL default false,
            start_year smallint NOT NULL check(start_year >= 1900),
            end_year smallint NOT NULL check(end_year >= 1900 and end_year >= start_year),
            create_date timestamp with time zone NOT NULL default now(),
            last_update_date timestamp with time zone NOT NULL default now(),
            PRIMARY KEY (season_id),
            UNIQUE (start_year, end_year)
        );
    """)

    op.execute("""
            CREATE TABLE IF NOT EXISTS league_season (
                league_season_id uuid NOT NULL UNIQUE,
                season_id uuid NOT NULL references season(season_id),
                external_season_id text NOT NULL,
                name text NOT NULL,
                league league_enum NOT NULL,
                last_update_date timestamp with time zone NOT NULL default now(),
                PRIMARY KEY (league_season_id),
                UNIQUE (external_season_id, league)
            );
        """)

    op.execute("CREATE INDEX IF NOT EXISTS idx_league_season_external_season_id ON league_season (external_season_id);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_league_season_season_id ON league_season (season_id);")

    op.execute("""
        CREATE TABLE IF NOT EXISTS division (
            division_id uuid NOT NULL UNIQUE,
            external_division_id text NOT NULL,
            name text NOT NULL check (length(name) >= 3),
            league league_enum NOT NULL,
            create_date timestamp with time zone NOT NULL default now(),
            season_id uuid NOT NULL references season(season_id),
            PRIMARY KEY (division_id),
            UNIQUE (external_division_id, league)
        );
    """)
    op.execute("CREATE INDEX IF NOT EXISTS idx_division_external_id ON division (external_division_id);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_division_season_id ON division (season_id);")

    op.execute("""
        CREATE TABLE IF NOT EXISTS team (
            team_id uuid NOT NULL UNIQUE,
            external_team_id text NOT NULL,
            team_name text NOT NULL,
            team_short_name text,
            team_name_abc text,
            region text,
            logo text,
            league league_enum,
            create_date timestamp with time zone NOT NULL default now(),
            PRIMARY KEY (team_id),
            UNIQUE (external_team_id, league)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS team_division (
            team_id uuid NOT NULL references team(team_id) ON DELETE CASCADE,
            division_id uuid NOT NULL references division(division_id) ON DELETE CASCADE,
            create_date timestamp with time zone NOT NULL default now(),
            PRIMARY KEY (team_id, division_id)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS player_profile (
            player_profile_id uuid NOT NULL UNIQUE,
            user_id uuid NOT NULL references "user"(user_id) ON DELETE CASCADE,
            profile_id text NOT NULL,
            first_name text NOT NULL check (length(first_name) >= 3),
            last_name text NOT NULL check (length(last_name) >= 3),
            middle_name text check (middle_name is null or length(middle_name) >= 3),
            player_height smallint check (player_height > 0 ),
            player_weight smallint check (player_height > 0 ),
            birthdate date,
            position smallint check(position >= 1 and position <= 5),
            player_rank smallint,
            photo text,
            player_number smallint check (player_number >= 0 and player_number < 100),
            league league_enum,
            parse_date timestamp with time zone NOT NULL,
            create_date timestamp with time zone NOT NULL default now(),
            last_update_date timestamp with time zone NOT NULL default now(),
            PRIMARY KEY (player_profile_id),
            UNIQUE (profile_id, league)
        );
    """)
    op.execute("CREATE INDEX IF NOT EXISTS idx_player_profile_profile_id ON player_profile (profile_id);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_player_profile_user_id ON player_profile (user_id);")

    op.execute("""
            CREATE TABLE IF NOT EXISTS player_team (
                player_profile_id uuid NOT NULL references player_profile(player_profile_id) ON DELETE CASCADE,
                team_id uuid NOT NULL references team(team_id) ON DELETE CASCADE,
                create_date timestamp with time zone NOT NULL default now(),
                PRIMARY KEY (player_profile_id, team_id)
            );
        """)

    op.execute("CREATE TYPE game_status_enum AS ENUM ('scheduled', 'live', 'finished');")

    op.execute("""
        CREATE TABLE IF NOT EXISTS game (
            game_id uuid NOT NULL UNIQUE,
            external_game_id text NOT NULL,
            division_id uuid NOT NULL references division(division_id) ON DELETE CASCADE,
            left_team_id uuid NULL references team(team_id) ON DELETE SET NULL,
            right_team_id uuid NULL references team(team_id) ON DELETE SET NULL,
            left_team_name text NOT NULL,
            right_team_name text NOT NULL,
            game_date timestamp with time zone,
            left_team_points smallint check (left_team_points >= 0),
            left_team_quarters_points jsonb,
            right_team_points smallint check (right_team_points >= 0),
            right_team_quarters_points jsonb,
            game_status game_status_enum NOT NULL default 'scheduled',
            game_place text,
            competition text,
            create_date timestamp with time zone NOT NULL default now(),
            last_update_date timestamp with time zone NOT NULL default now(),
            PRIMARY KEY (game_id)
        );
    """)
    op.execute("CREATE INDEX IF NOT EXISTS idx_game_external_game_id ON game (external_game_id);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_game_game_date ON game (game_date);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_game_division_id ON game (division_id);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_game_left_team_id ON game (left_team_id);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_game_right_team_id ON game (right_team_id);")

    op.execute("""
        CREATE TABLE IF NOT EXISTS player_game_statistics (
            player_game_statistics_id uuid NOT NULL UNIQUE,
            player_profile_id uuid NOT NULL references player_profile(player_profile_id) ON DELETE CASCADE,
            game_id uuid NOT NULL references game(game_id),
            player_number smallint check (player_number >= 0 and player_number < 100),
            total_points smallint NOT NULL DEFAULT 0 check (total_points >= 0 and total_points <= 1000),
            points_1 smallint NOT NULL DEFAULT 0 check (points_1 >= 0 and points_1 <= 100),
            shots_1 smallint NOT NULL DEFAULT 0 check (shots_1 >= 0 and shots_1 <= 100),
            points_2 smallint NOT NULL DEFAULT 0 check (points_2 >= 0 and points_2 <= 100),
            shots_2 smallint NOT NULL DEFAULT 0 check (shots_2 >= 0 and shots_2 <= 100),
            points_3 smallint NOT NULL DEFAULT 0 check (points_3 >= 0 and points_3 <= 100),
            shots_3 smallint NOT NULL DEFAULT 0 check (shots_3 >= 0 and shots_3 <= 100),
            assists smallint NOT NULL DEFAULT 0 check (assists >= 0 and assists <= 100),
            blocks smallint NOT NULL DEFAULT 0 check (blocks >= 0 and blocks <= 100),
            defence_rebounds smallint NOT NULL DEFAULT 0 check (defence_rebounds >= 0 and defence_rebounds <= 100),
            offence_rebounds smallint NOT NULL DEFAULT 0 check (offence_rebounds >= 0 and offence_rebounds <= 100),
            steals smallint NOT NULL DEFAULT 0 check (steals >= 0 and steals <= 100),
            turnovers smallint NOT NULL DEFAULT 0 check (turnovers >= 0 and turnovers <= 100),
            fouls smallint NOT NULL DEFAULT 0 check (fouls >= 0 and fouls <= 7),
            opponent_fouls smallint NOT NULL DEFAULT 0 check (opponent_fouls >= 0 and opponent_fouls <= 100),
            played_time_seconds smallint NOT NULL DEFAULT 0 check
            (played_time_seconds >= 0 and played_time_seconds <= 7200),
            plus_minus smallint NOT NULL DEFAULT 0 check (plus_minus >= -500 and plus_minus <= 500),
            is_start boolean DEFAULT false,
            kpi smallint NOT NULL DEFAULT 0 check (kpi >= -500 and kpi <= 500),
            create_date timestamp with time zone NOT NULL default now(),
            PRIMARY KEY (player_game_statistics_id),
            UNIQUE (player_profile_id, game_id)
        );
    """)
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_player_game_statistics_profile_id ON "
        "player_game_statistics (player_profile_id);"
    )
    op.execute("CREATE INDEX IF NOT EXISTS idx_player_game_statistics_game_id ON player_game_statistics (game_id);")


def downgrade() -> None:
    """Downgrade schema."""
    # Drop tables in reverse dependency order (children first).
    # Indexes are dropped automatically with their tables.
    op.execute("DROP TABLE IF EXISTS player_game_statistics;")
    op.execute("DROP TABLE IF EXISTS player_team;")
    op.execute("DROP TABLE IF EXISTS game;")
    op.execute("DROP TABLE IF EXISTS player_profile;")
    op.execute("DROP TABLE IF EXISTS team_division;")
    op.execute("DROP TABLE IF EXISTS division;")
    op.execute("DROP TABLE IF EXISTS league_season;")
    op.execute("DROP TABLE IF EXISTS team;")
    op.execute("DROP TABLE IF EXISTS season;")
    op.execute("DROP TABLE IF EXISTS user_agreement;")
    op.execute("DROP TABLE IF EXISTS user_info;")
    op.execute('DROP TABLE IF EXISTS "user";')
    # Drop custom types (after all tables that use them are dropped).
    op.execute("DROP TYPE IF EXISTS game_status_enum;")
    op.execute("DROP TYPE IF EXISTS league_enum;")
    op.execute("DROP TYPE IF EXISTS gender_enum;")
