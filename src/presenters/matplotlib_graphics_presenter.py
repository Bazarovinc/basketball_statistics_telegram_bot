from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
from loguru import logger
from matplotlib.axes import Axes
from matplotlib.container import BarContainer
from pandas import DataFrame

from common.domain.dto.statistics_presenter import StatisticsPresenterSchema
from src.constants import (
    ASSISTS_COLOR,
    ASSISTS_NAME,
    ASSISTS_TURNOVERS_STEALS_TITLE,
    BAR_TEXT_HA,
    BAR_TEXT_VA,
    BAR_WIDTH_3_BARS,
    DEFENCE_REBOUNDS_COLOR,
    DEFENCE_REBOUNDS_NAME,
    FONTSIZE,
    FOULS_COLOR,
    FOULS_NAME,
    FOULS_TITLE,
    IMAGE_HEIGHT,
    IMAGE_TYPE,
    IMAGE_WIDTH,
    KPI_TITLE,
    MEAN_KPI_LABEL,
    MEAN_POINTS_LABEL,
    NEGATIVE_KPI_COLOR,
    OFFENCE_REBOUNDS_COLOR,
    OFFENCE_REBOUNDS_NAME,
    OPPONENT_FOULS_COLOR,
    OPPONENT_FOULS_NAME,
    POINTS_1_COLOR,
    POINTS_2_COLOR,
    POINTS_3_COLOR,
    POINTS_COLORS,
    POINTS_NAMES,
    POSITIVE_KPI_COLOR,
    REBOUNDS_TITLE,
    RELEASE_1_PERCENT_NAME,
    RELEASE_2_PERCENT_NAME,
    RELEASE_3_PERCENT_NAME,
    SCORES_PERCENT_TITLE,
    SHOTS_COLORS,
    SHOTS_NAMES,
    SHOTS_TITLE,
    STEALS_COLOR,
    STEALS_NAME,
    TOTAL_SCORE_COLOR,
    TOTAL_SCORE_TITLE,
    TURNOVERS_COLOR,
    TURNOVERS_NAME,
)
from src.presenters.interfaces import MultiplyDataPresenter

MIN_GROUPED_BARS: int = 2


class MatplotlibGraphicsPresenter(MultiplyDataPresenter):
    @staticmethod
    def _draw_statistic(ax: Axes, title: str) -> bytes:
        """Отрисовка графика на предоставленных осях и сохранение в bytes."""
        ax.set_title(title)
        ax.legend()
        buf = BytesIO()
        plt.savefig(buf, format=IMAGE_TYPE, dpi=100, bbox_inches="tight")
        buf.seek(0)
        plt.close()
        return buf.getvalue()

    @staticmethod
    def _setup_axes(data: DataFrame) -> tuple[plt.Figure, plt.Axes]:
        """Создание фигуры и осей с настройками размера."""
        plt.ioff()
        fig, ax = plt.subplots(figsize=(IMAGE_WIDTH / 100, IMAGE_HEIGHT / 100))

        # Настройка сетки
        ax.grid(
            visible=True,
            linestyle="--",
            linewidth=0.5,
            alpha=0.7,
            color="gray",
            zorder=0,  # Убедимся, что сетка под графиками
        )
        ax.set_xticks(np.arange(len(data)))
        ax.set_xticklabels(data["game_info"], rotation=45, ha="right")  # Поворот подписей
        return fig, ax

    def _plot_grouped_bars(
        self,
        ax: Axes,
        data: DataFrame,
        groups: tuple[tuple, ...],
        bar_width: float,
        fontsize: float,
        rotation: int = None,
    ) -> None:
        """Отрисовка сгруппированных столбцов."""
        x = np.arange(len(data))
        positions = (-(bar_width / 2), bar_width / 2) if len(groups) == MIN_GROUPED_BARS else (-bar_width, 0, bar_width)
        for (_, (values, name, color)), position in zip(enumerate(groups), positions):
            pos = x + position
            bars = ax.bar(pos, values, width=bar_width, label=name, color=color)
            self._add_labels(ax, bars, pos, fontsize, rotation)

    @staticmethod
    def _add_labels(ax: Axes, bars: BarContainer, positions: np.ndarray, fontsize: float, rotation: int = None) -> None:
        """Добавление текстовых меток над столбцами."""
        for bar, pos in zip(bars, positions):
            height = bar.get_height()
            ax.text(
                pos,
                height,
                f"{height}",
                ha=BAR_TEXT_HA,
                va=BAR_TEXT_VA,
                fontsize=fontsize,
                rotation=rotation,
            )

    def _draw_shots_and_points(self, data: DataFrame) -> bytes:
        """Отрисовка столбцов points_{1-3} поверх shots_{1-3}."""
        fig, ax = self._setup_axes(data)
        x = np.arange(len(data))  # Позиции по оси X

        for point_score, place in zip(range(1, 4), (-1, 0, 1)):
            ax.bar(
                x + place * BAR_WIDTH_3_BARS,
                data[f"shots_{point_score}"],
                width=BAR_WIDTH_3_BARS,
                label=SHOTS_NAMES.get(point_score),
                color=SHOTS_COLORS.get(point_score),
            )
            ax.bar(
                x + place * BAR_WIDTH_3_BARS,
                data[f"points_{point_score}"],
                width=BAR_WIDTH_3_BARS,
                label=POINTS_NAMES.get(point_score),
                color=POINTS_COLORS.get(point_score),
            )

            for i, (points, shots) in enumerate(zip(data[f"points_{point_score}"], data[f"shots_{point_score}"])):
                if shots != points:
                    ax.text(
                        x[i] + place * BAR_WIDTH_3_BARS,
                        shots,
                        f"{shots}",
                        ha=BAR_TEXT_HA,
                        va=BAR_TEXT_VA,
                        fontsize=FONTSIZE,
                    )
                ax.text(
                    x[i] + place * BAR_WIDTH_3_BARS,
                    points,
                    f"{points}",
                    ha=BAR_TEXT_HA,
                    va=BAR_TEXT_VA,
                    fontsize=FONTSIZE,
                )
        return self._draw_statistic(ax, SHOTS_TITLE)

    def _draw_multiply_bars(
        self,
        data: DataFrame,
        groups: tuple[tuple[np.array, str, str], ...],
        title: str,
        bar_width: float = 0.2,
        fontsize: float = FONTSIZE,
        rotation: int = None,
    ) -> bytes:
        fig, ax = self._setup_axes(data)
        self._plot_grouped_bars(ax, data, groups, bar_width, fontsize, rotation)
        return self._draw_statistic(ax, title)

    def _draw_single_bar(
        self, data: DataFrame, y_name: str, color: str, title: str, mean_label: str = "Среднее: {mean_value:.2f}"
    ) -> bytes:
        """Отрисовка одиночного столбца с линией среднего значения."""
        fig, ax = self._setup_axes(data)
        bars = ax.bar(data["game_info"], data[y_name], color=color)
        self._add_labels(ax, bars, np.arange(len(data)), FONTSIZE)

        # Добавление пунктирной линии среднего значения
        mean_value = data[y_name].mean()

        ax.axhline(
            y=mean_value,
            color="blue",
            linestyle="--",
            linewidth=2,
            alpha=0.8,
            label=mean_label.format(mean_value=mean_value),
        )
        return self._draw_statistic(ax, title)

    def _draw_kpi_graphic(self, data: DataFrame) -> bytes:
        """Отрисовка KPI с линией среднего значения."""
        fig, ax = self._setup_axes(data)
        colors = [POSITIVE_KPI_COLOR if kpi > 0 else NEGATIVE_KPI_COLOR for kpi in data["kpi"]]
        bars = ax.bar(data["game_info"], data["kpi"], color=colors)
        self._add_labels(ax, bars, np.arange(len(data)), FONTSIZE)

        # Добавление пунктирной линии среднего значения KPI
        mean_kpi = data["kpi"].mean()
        ax.axhline(
            y=mean_kpi,
            color="green",
            linestyle="--",
            linewidth=2,
            alpha=0.8,
            label=MEAN_KPI_LABEL.format(mean_value=mean_kpi),
        )

        return self._draw_statistic(ax, KPI_TITLE)

    @staticmethod
    def _prepare_data(data: DataFrame) -> None:
        columns = set(data.columns)
        if len({"shots_1_percent", "shots_2_percent", "shots_3_percent"} - columns) > 0:
            data["shots_1_percent"] = round(data["points_1"] / data["shots_1"] * 100, 2)
            data["shots_2_percent"] = round(data["points_2"] / data["shots_2"] * 100, 2)
            data["shots_3_percent"] = round(data["points_3"] / data["shots_3"] * 100, 2)
        if len({"shots_1_percent_name", "shots_2_percent_name", "shots_3_percent_name"} - columns) > 0:
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

    def __call__(self, data: tuple[StatisticsPresenterSchema, ...]) -> tuple[tuple[bytes, str], ...]:
        logger.info("Построение графиков")
        converted_data = DataFrame([vars(s) for s in data])
        self._prepare_data(converted_data)
        # Для каждого графика создаем отдельную фигуру
        return (
            (self._draw_shots_and_points(converted_data), SHOTS_TITLE),
            (
                self._draw_single_bar(
                    converted_data, "total_points", TOTAL_SCORE_COLOR, TOTAL_SCORE_TITLE, MEAN_POINTS_LABEL
                ),
                TOTAL_SCORE_TITLE,
            ),
            (
                self._draw_multiply_bars(
                    converted_data,
                    (
                        (converted_data["shots_1_percent"], RELEASE_1_PERCENT_NAME, POINTS_1_COLOR),
                        (converted_data["shots_2_percent"], RELEASE_2_PERCENT_NAME, POINTS_2_COLOR),
                        (converted_data["shots_3_percent"], RELEASE_3_PERCENT_NAME, POINTS_3_COLOR),
                    ),
                    SCORES_PERCENT_TITLE,
                    0.3,
                    # 10,
                    rotation=90,
                ),
                SCORES_PERCENT_TITLE,
            ),
            (
                self._draw_multiply_bars(
                    converted_data,
                    (
                        (
                            converted_data["defence_rebounds"],
                            DEFENCE_REBOUNDS_NAME,
                            DEFENCE_REBOUNDS_COLOR,
                        ),
                        (
                            converted_data["offence_rebounds"],
                            OFFENCE_REBOUNDS_NAME,
                            OFFENCE_REBOUNDS_COLOR,
                        ),
                    ),
                    REBOUNDS_TITLE,
                    0.4,
                ),
                REBOUNDS_TITLE,
            ),
            (
                self._draw_multiply_bars(
                    converted_data,
                    (
                        (converted_data["assists"], ASSISTS_NAME, ASSISTS_COLOR),
                        (converted_data["turnovers"], TURNOVERS_NAME, TURNOVERS_COLOR),
                        (converted_data["steals"], STEALS_NAME, STEALS_COLOR),
                    ),
                    ASSISTS_TURNOVERS_STEALS_TITLE,
                    BAR_WIDTH_3_BARS,
                ),
                ASSISTS_TURNOVERS_STEALS_TITLE,
            ),
            (
                self._draw_multiply_bars(
                    converted_data,
                    (
                        (converted_data["fouls"], FOULS_NAME, FOULS_COLOR),
                        (
                            converted_data["opponent_fouls"],
                            OPPONENT_FOULS_NAME,
                            OPPONENT_FOULS_COLOR,
                        ),
                    ),
                    FOULS_TITLE,
                    0.4,
                ),
                FOULS_TITLE,
            ),
            (self._draw_kpi_graphic(converted_data), KPI_TITLE),
        )
