from typing import Final

_RED: Final[str] = "#DC3912"
_BLUE: Final[str] = "#3366CC"
_GREEN: Final[str] = "#109618"

SHOTS_1_COLOR: Final[str] = "#0099C6"
SHOTS_1_NAME: Final[str] = "Штрафных брошено"
POINTS_1_COLOR: Final[str] = _GREEN
POINTS_1_NAME: Final[str] = "Штрафных забито"
RELEASE_1_PERCENT_NAME: Final[str] = "% реализации штрафных бросков"

SHOTS_2_COLOR: Final[str] = "#DD4477"
SHOTS_2_NAME: Final[str] = "2-ух очковых брошено"
POINTS_2_COLOR: Final[str] = _BLUE
POINTS_2_NAME: Final[str] = "2-ух очковых забито"
RELEASE_2_PERCENT_NAME: Final[str] = "% реализации 2-ух очковых бросков"

SHOTS_3_COLOR: Final[str] = "#990099"
SHOTS_3_NAME: Final[str] = "3-ех очковых брошено"
POINTS_3_COLOR: Final[str] = _RED
POINTS_3_NAME: Final[str] = "3-ех очковых забито"
RELEASE_3_PERCENT_NAME: Final[str] = "% реализации 3-ех очковых бросков"

SHOTS_COLORS: Final[dict[int, str]] = {
    1: SHOTS_1_COLOR,
    2: SHOTS_2_COLOR,
    3: SHOTS_3_COLOR,
}

POINTS_COLORS: Final[dict[int, str]] = {
    1: POINTS_1_COLOR,
    2: POINTS_2_COLOR,
    3: POINTS_3_COLOR,
}

POINTS_NAMES: Final[dict[int, str]] = {
    1: POINTS_1_NAME,
    2: POINTS_2_NAME,
    3: POINTS_3_NAME,
}

SHOTS_NAMES: Final[dict[int, str]] = {
    1: SHOTS_1_NAME,
    2: SHOTS_2_NAME,
    3: SHOTS_3_NAME,
}


SHOTS_TITLE: Final[str] = "Реализация бросков"
TOTAL_SCORE_COLOR: Final[str] = _RED
TOTAL_SCORE_TITLE: Final[str] = "Набрано очков"
SCORES_PERCENT_TITLE: Final[str] = "Процент реализации бросков"


DEFENCE_REBOUNDS_COLOR: Final[str] = _BLUE
DEFENCE_REBOUNDS_NAME: Final[str] = "Подборы в защите"
OFFENCE_REBOUNDS_COLOR: Final[str] = _RED
OFFENCE_REBOUNDS_NAME: Final[str] = "Подборы в нападении"
REBOUNDS_TITLE: Final[str] = "Подборы"

ASSISTS_COLOR: Final[str] = _BLUE
ASSISTS_NAME: Final[str] = "Голевые передачи"
TURNOVERS_COLOR: Final[str] = _RED
TURNOVERS_NAME: Final[str] = "Потери"
STEALS_COLOR: Final[str] = _GREEN
STEALS_NAME: Final[str] = "Перехваты"
ASSISTS_TURNOVERS_STEALS_TITLE: Final[str] = "Передачи/потери/перехваты"


FOULS_COLOR: Final[str] = _BLUE
FOULS_NAME: Final[str] = "Фолы"
OPPONENT_FOULS_COLOR: Final[str] = _RED
OPPONENT_FOULS_NAME: Final[str] = "Фолы соперника"
FOULS_TITLE: Final[str] = "Фолы"

POSITIVE_KPI_COLOR: Final[str] = _RED
NEGATIVE_KPI_COLOR: Final[str] = _BLUE
KPI_TITLE: Final[str] = "КПИ (коэффициент полезности игрока)"


IMAGE_TYPE: Final[str] = "png"
IMAGE_WIDTH: Final[int] = 1800
IMAGE_HEIGHT: Final[int] = 1200

FONTSIZE: Final[int] = 15
BAR_WIDTH_3_BARS: Final[float] = 0.3

BAR_TEXT_HA: Final[str] = "center"
BAR_TEXT_VA: Final[str] = "bottom"

MEAN_KPI_LABEL: Final[str] = "Средний KPI: {mean_value:.2f}"
MEAN_POINTS_LABEL: Final[str] = "Среднее число набираемых очков: {mean_value:.2f}"
