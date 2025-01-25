import numpy as np
from loguru import logger
from pandas import DataFrame
from plotly.graph_objects import Bar, Figure

from common.domain.dto.statistics_presenter import StatisticPresenterBaseSchema
from src.constants import (
    ASSISTS_COLOR,
    ASSISTS_NAME,
    ASSISTS_TURNOVERS_STEALS_TITLE,
    DEFENCE_REBOUNDS_COLOR,
    DEFENCE_REBOUNDS_NAME,
    FOULS_COLOR,
    FOULS_NAME,
    FOULS_TITLE,
    IMAGE_HEIGHT,
    IMAGE_TYPE,
    IMAGE_WIDTH,
    KPI_TITLE,
    NEGATIVE_KPI_COLOR,
    OFFENCE_REBOUNDS_COLOR,
    OFFENCE_REBOUNDS_NAME,
    OPPONENT_FOULS_COLOR,
    OPPONENT_FOULS_NAME,
    POINTS_1_COLOR,
    POINTS_1_NAME,
    POINTS_2_COLOR,
    POINTS_2_NAME,
    POINTS_3_COLOR,
    POINTS_3_NAME,
    POSITIVE_KPI_COLOR,
    REBOUNDS_TITLE,
    RELEASE_1_PERCENT_NAME,
    RELEASE_2_PERCENT_NAME,
    RELEASE_3_PERCENT_NAME,
    SCORES_PERCENT_TITLE,
    SHOTS_1_COLOR,
    SHOTS_1_NAME,
    SHOTS_2_COLOR,
    SHOTS_2_NAME,
    SHOTS_3_COLOR,
    SHOTS_3_NAME,
    SHOTS_TITLE,
    STEALS_COLOR,
    STEALS_NAME,
    TOTAL_SCORE_COLOR,
    TOTAL_SCORE_TITLE,
    TURNOVERS_COLOR,
    TURNOVERS_NAME,
)
from src.presenters.interfaces import MultiplyDataPresenter


class PlotlyGraphicsPresenter(MultiplyDataPresenter):

    def _draw_statistic(self, data_for_figure: tuple[Bar, ...] | Bar, title: str) -> bytes:
        logger.info(f"Построение графика {title}")
        fig = Figure(data=data_for_figure)
        fig.update_layout(title_text=title)
        # fig.show()
        return fig.to_image(format=IMAGE_TYPE, width=IMAGE_WIDTH, height=IMAGE_HEIGHT)

    def _get_shots_and_points_bars(self, data: DataFrame) -> tuple[Bar, ...]:
        return (
            Bar(
                y=data["shots_1"],
                x=data["game_info"],
                name=SHOTS_1_NAME,
                offsetgroup=0,
                textposition="auto",
                text=data["shots_1"],
                marker_color=SHOTS_1_COLOR,
            ),
            Bar(
                y=data["points_1"],
                x=data["game_info"],
                name=POINTS_1_NAME,
                offsetgroup=0,
                textposition="auto",
                text=data["points_1"],
                marker_color=POINTS_1_COLOR,
            ),
            Bar(
                y=data["shots_2"],
                x=data["game_info"],
                name=SHOTS_2_NAME,
                offsetgroup=1,
                textposition="auto",
                text=data["shots_2"],
                marker_color=SHOTS_2_COLOR,
            ),
            Bar(
                y=data["points_2"],
                x=data["game_info"],
                name=POINTS_2_NAME,
                offsetgroup=1,
                textposition="auto",
                text=data["points_2"],
                marker_color=POINTS_2_COLOR,
            ),
            Bar(
                y=data["shots_3"],
                x=data["game_info"],
                name=SHOTS_3_NAME,
                offsetgroup=2,
                textposition="auto",
                text=data["shots_3"],
                marker_color=SHOTS_3_COLOR,
            ),
            Bar(
                y=data["points_3"],
                x=data["game_info"],
                name=POINTS_3_NAME,
                offsetgroup=2,
                textposition="auto",
                text=data["points_3"],
                marker_color=POINTS_3_COLOR,
            ),
        )

    def _get_total_score_bars(self, data: DataFrame) -> tuple[Bar, ...]:
        return (
            Bar(
                y=data["total_points"],
                x=data["game_info"],
                offsetgroup=0,
                textposition="auto",
                text=data["total_points"],
                marker_color=TOTAL_SCORE_COLOR,
            ),
        )

    def _get_shots_percent_bars(self, data: DataFrame) -> tuple[Bar, ...]:
        return (
            Bar(
                y=data["shots_1_percent"],
                x=data["game_info"],
                name=RELEASE_1_PERCENT_NAME,
                offsetgroup=0,
                textposition="auto",
                text=data["shots_1_percent_name"],
                marker_color=POINTS_1_COLOR,
            ),
            Bar(
                y=data["shots_2_percent"],
                x=data["game_info"],
                name=RELEASE_2_PERCENT_NAME,
                offsetgroup=1,
                textposition="auto",
                text=data["shots_2_percent_name"],
                marker_color=POINTS_2_COLOR,
            ),
            Bar(
                y=data["shots_3_percent"],
                x=data["game_info"],
                name=RELEASE_3_PERCENT_NAME,
                offsetgroup=2,
                textposition="auto",
                text=data["shots_3_percent_name"],
                marker_color=POINTS_3_COLOR,
            ),
        )

    def _prepare_data(self, data: DataFrame) -> None:
        columns = set(data.columns)
        if len({"shots_1_percent", "shots_2_percent", "shots_3_percent"} - columns) > 0:
            data["shots_1_percent"] = round(data["points_1"] / data["shots_1"] * 100, 2)
            data["shots_2_percent"] = round(data["points_2"] / data["shots_2"] * 100, 2)
            data["shots_3_percent"] = round(data["points_3"] / data["shots_3"] * 100, 2)
        if (
            len({"shots_1_percent_name", "shots_2_percent_name", "shots_3_percent_name"} - columns)
            > 0
        ):
            data["shots_1_percent_name"] = (
                data["points_1"].astype(str)
                + "/"
                + data["shots_1"].astype(str)
                + " "
                + data["shots_1_percent"].astype(str)
                + "%"
            )
            data["shots_2_percent_name"] = (
                data["points_2"].astype(str)
                + "/"
                + data["shots_2"].astype(str)
                + " "
                + data["shots_2_percent"].astype(str)
                + "%"
            )
            data["shots_3_percent_name"] = (
                data["points_3"].astype(str)
                + "/"
                + data["shots_3"].astype(str)
                + " "
                + data["shots_3_percent"].astype(str)
                + "%"
            )
        data["kpi_color"] = np.where(data["kpi"] > 0, POSITIVE_KPI_COLOR, NEGATIVE_KPI_COLOR)

    def _get_rebounds_bars(self, data: DataFrame) -> tuple[Bar, ...]:
        return (
            Bar(
                y=data["defence_rebounds"],
                x=data["game_info"],
                name=DEFENCE_REBOUNDS_NAME,
                textposition="auto",
                text=data["defence_rebounds"],
                marker_color=DEFENCE_REBOUNDS_COLOR,
            ),
            Bar(
                y=data["offence_rebounds"],
                x=data["game_info"],
                name=OFFENCE_REBOUNDS_NAME,
                textposition="auto",
                text=data["offence_rebounds"],
                marker_color=OFFENCE_REBOUNDS_COLOR,
            ),
        )

    def _get_assists_bars(self, data: DataFrame) -> tuple[Bar, ...]:
        return (
            Bar(
                y=data["assists"],
                x=data["game_info"],
                name=ASSISTS_NAME,
                textposition="auto",
                text=data["assists"],
                marker_color=ASSISTS_COLOR,
            ),
            Bar(
                y=data["turnovers"],
                x=data["game_info"],
                name=TURNOVERS_NAME,
                textposition="auto",
                text=data["turnovers"],
                marker_color=TURNOVERS_COLOR,
            ),
            Bar(
                y=data["steals"],
                x=data["game_info"],
                name=STEALS_NAME,
                textposition="auto",
                text=data["steals"],
                marker_color=STEALS_COLOR,
            ),
        )

    def _get_fouls_bars(self, data: DataFrame) -> tuple[Bar, ...]:
        return (
            Bar(
                y=data["fouls"],
                x=data["game_info"],
                name=FOULS_NAME,
                textposition="auto",
                text=data["fouls"],
                marker_color=FOULS_COLOR,
            ),
            Bar(
                y=data["opponent_fouls"],
                x=data["game_info"],
                name=OPPONENT_FOULS_NAME,
                textposition="auto",
                text=data["opponent_fouls"],
                marker_color=OPPONENT_FOULS_COLOR,
            ),
        )

    def _get_kpi_bars(self, data: DataFrame) -> tuple[Bar, ...]:
        return (
            Bar(
                y=data["kpi"],
                x=data["game_info"],
                textposition="auto",
                text=data["kpi"],
                marker_color=data["kpi_color"],
                # marker_color=KPI_COLOR,
            ),
        )

    def __call__(
        self, data: tuple[StatisticPresenterBaseSchema, ...]
    ) -> tuple[tuple[bytes, str], ...]:
        logger.info("Построение графиков")
        converted_data = DataFrame([vars(s) for s in data])
        self._prepare_data(converted_data)
        result = (
            (
                self._draw_statistic(self._get_shots_and_points_bars(converted_data), SHOTS_TITLE),
                SHOTS_TITLE,
            ),
            (
                self._draw_statistic(self._get_total_score_bars(converted_data), TOTAL_SCORE_TITLE),
                TOTAL_SCORE_TITLE,
            ),
            (
                self._draw_statistic(
                    self._get_shots_percent_bars(converted_data), SCORES_PERCENT_TITLE
                ),
                SCORES_PERCENT_TITLE,
            ),
            (
                self._draw_statistic(self._get_rebounds_bars(converted_data), REBOUNDS_TITLE),
                REBOUNDS_TITLE,
            ),
            (
                self._draw_statistic(
                    self._get_assists_bars(converted_data), ASSISTS_TURNOVERS_STEALS_TITLE
                ),
                ASSISTS_TURNOVERS_STEALS_TITLE,
            ),
            (self._draw_statistic(self._get_fouls_bars(converted_data), FOULS_TITLE), FOULS_TITLE),
            (self._draw_statistic(self._get_kpi_bars(converted_data), KPI_TITLE), KPI_TITLE),
        )
        logger.info("Все графики построены")
        return result
