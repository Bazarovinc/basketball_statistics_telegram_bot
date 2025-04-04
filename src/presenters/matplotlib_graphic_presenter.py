from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
from loguru import logger
from matplotlib.axes import Axes
from pandas import DataFrame

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


class MatplotlibGraphicsPresenter(MultiplyDataPresenter):
    def _draw_statistic(self, ax: Axes, title: str) -> bytes:
        """Отрисовка графика на предоставленных осях и сохранение в bytes."""
        ax.set_title(title)
        buf = BytesIO()
        plt.savefig(buf, format=IMAGE_TYPE, dpi=100, bbox_inches="tight")
        buf.seek(0)
        plt.close()
        return buf.getvalue()

    def _setup_axes(self) -> tuple[plt.Figure, plt.Axes]:
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
        return fig, ax

    def _plot_grouped_bars(self, ax: Axes, data: DataFrame, groups: list[tuple], bar_width=0.2):
        """Отрисовка сгруппированных столбцов."""
        x = np.arange(len(data))
        for i, (values, name, color) in enumerate(groups):
            pos = x + i * bar_width - (len(groups) * bar_width) / 2
            bars = ax.bar(pos, values, width=bar_width, label=name, color=color)
            self._add_labels(ax, bars, pos)

    def _add_labels(self, ax: Axes, bars, positions):
        """Добавление текстовых меток над столбцами."""
        for bar, pos in zip(bars, positions):
            height = bar.get_height()
            ax.text(pos, height, f"{height}", ha="center", va="bottom")

    def _get_shots_and_points_bars(self, ax: Axes, data: DataFrame) -> None:
        """Отрисовка столбцов points_{1-3} поверх shots_{1-3}."""
        x = np.arange(len(data))  # Позиции по оси X
        bar_width = 0.2  # Ширина столбцов

        # Отрисовка shots_{1-3}
        shots_bars = ax.bar(
            x - bar_width, data["shots_1"], width=bar_width, label=SHOTS_1_NAME, color=SHOTS_1_COLOR
        )
        ax.bar(x, data["shots_2"], width=bar_width, label=SHOTS_2_NAME, color=SHOTS_2_COLOR)
        ax.bar(
            x + bar_width, data["shots_3"], width=bar_width, label=SHOTS_3_NAME, color=SHOTS_3_COLOR
        )

        # Отрисовка points_{1-3} поверх shots_{1-3}
        ax.bar(
            x - bar_width,
            data["points_1"],
            width=bar_width,
            label=POINTS_1_NAME,
            color=POINTS_1_COLOR,
            bottom=data["shots_1"],  # Начинаем от верха shots_1
        )
        ax.bar(
            x,
            data["points_2"],
            width=bar_width,
            label=POINTS_2_NAME,
            color=POINTS_2_COLOR,
            bottom=data["shots_2"],  # Начинаем от верха shots_2
        )
        ax.bar(
            x + bar_width,
            data["points_3"],
            width=bar_width,
            label=POINTS_3_NAME,
            color=POINTS_3_COLOR,
            bottom=data["shots_3"],  # Начинаем от верха shots_3
        )

        # Настройка осей и легенды
        ax.set_xticks(x)
        ax.set_xticklabels(data["game_info"], rotation=45, ha="right")  # Поворот подписей
        ax.legend()

        # Добавление аннотаций для shots_{1-3}
        for bar in shots_bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{height}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

        # Добавление аннотаций для points_{1-3}
        for i, (points, shots) in enumerate(zip(data["points_1"], data["shots_1"])):
            ax.text(
                x[i] - bar_width, shots + points, f"{points}", ha="center", va="bottom", fontsize=8
            )
        for i, (points, shots) in enumerate(zip(data["points_2"], data["shots_2"])):
            ax.text(x[i], shots + points, f"{points}", ha="center", va="bottom", fontsize=8)
        for i, (points, shots) in enumerate(zip(data["points_3"], data["shots_3"])):
            ax.text(
                x[i] + bar_width, shots + points, f"{points}", ha="center", va="bottom", fontsize=8
            )

    def _get_total_score_bars(self, ax: Axes, data: DataFrame) -> None:
        bars = ax.bar(data["game_info"], data["total_points"], color=TOTAL_SCORE_COLOR)
        self._add_labels(ax, bars, np.arange(len(data)))

    def _get_shots_percent_bars(self, ax: Axes, data: DataFrame) -> None:
        groups = [
            (data["shots_1_percent"], RELEASE_1_PERCENT_NAME, POINTS_1_COLOR),
            (data["shots_2_percent"], RELEASE_2_PERCENT_NAME, POINTS_2_COLOR),
            (data["shots_3_percent"], RELEASE_3_PERCENT_NAME, POINTS_3_COLOR),
        ]
        self._plot_grouped_bars(ax, data, groups)
        ax.set_xticks(np.arange(len(data)))
        ax.set_xticklabels(data["game_info"])
        ax.legend()

    def _get_rebounds_bars(self, ax: Axes, data: DataFrame) -> None:
        width = 0.4
        x = np.arange(len(data))
        ax.bar(
            x - width / 2,
            data["defence_rebounds"],
            width,
            label=DEFENCE_REBOUNDS_NAME,
            color=DEFENCE_REBOUNDS_COLOR,
        )
        ax.bar(
            x + width / 2,
            data["offence_rebounds"],
            width,
            label=OFFENCE_REBOUNDS_NAME,
            color=OFFENCE_REBOUNDS_COLOR,
        )
        ax.set_xticks(x)
        ax.set_xticklabels(data["game_info"])
        ax.legend()
        self._add_labels(ax, ax.patches, x - width / 2)
        self._add_labels(ax, ax.patches[len(data):], x + width / 2)

    def _get_assists_bars(self, ax: Axes, data: DataFrame) -> None:
        x = np.arange(len(data))
        width = 0.25
        ax.bar(x - width, data["assists"], width, label=ASSISTS_NAME, color=ASSISTS_COLOR)
        ax.bar(x, data["turnovers"], width, label=TURNOVERS_NAME, color=TURNOVERS_COLOR)
        ax.bar(x + width, data["steals"], width, label=STEALS_NAME, color=STEALS_COLOR)
        ax.set_xticks(x)
        ax.set_xticklabels(data["game_info"])
        ax.legend()

        # Исправление: используем индекс контейнера для расчета позиции
        for i, container in enumerate(ax.containers):
            offset = x - width + (i * width)
            self._add_labels(ax, container, offset)

    def _get_fouls_bars(self, ax: Axes, data: DataFrame) -> None:
        width = 0.4
        x = np.arange(len(data))
        ax.bar(x - width / 2, data["fouls"], width, label=FOULS_NAME, color=FOULS_COLOR)
        ax.bar(
            x + width / 2,
            data["opponent_fouls"],
            width,
            label=OPPONENT_FOULS_NAME,
            color=OPPONENT_FOULS_COLOR,
        )
        ax.set_xticks(x)
        ax.set_xticklabels(data["game_info"])
        ax.legend()
        self._add_labels(ax, ax.patches, x - width / 2)
        self._add_labels(ax, ax.patches[len(data):], x + width / 2)

    def _get_kpi_bars(self, ax: Axes, data: DataFrame) -> None:
        colors = [POSITIVE_KPI_COLOR if kpi > 0 else NEGATIVE_KPI_COLOR for kpi in data["kpi"]]
        bars = ax.bar(data["game_info"], data["kpi"], color=colors)
        self._add_labels(ax, bars, np.arange(len(data)))

    def _prepare_data(self, data: DataFrame) -> None:
        # Оригинальная логика подготовки данных
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

    def __call__(
        self, data: tuple[StatisticPresenterBaseSchema, ...]
    ) -> tuple[tuple[bytes, str], ...]:
        logger.info("Построение графиков")
        converted_data = DataFrame([vars(s) for s in data])
        self._prepare_data(converted_data)

        result = []
        # Для каждого графика создаем отдельную фигуру
        fig, ax = self._setup_axes()
        self._get_shots_and_points_bars(ax, converted_data)
        result.append((self._draw_statistic(ax, SHOTS_TITLE), SHOTS_TITLE))

        fig, ax = self._setup_axes()
        self._get_total_score_bars(ax, converted_data)
        result.append((self._draw_statistic(ax, TOTAL_SCORE_TITLE), TOTAL_SCORE_TITLE))

        fig, ax = self._setup_axes()
        self._get_shots_percent_bars(ax, converted_data)
        result.append((self._draw_statistic(ax, SCORES_PERCENT_TITLE), SCORES_PERCENT_TITLE))

        fig, ax = self._setup_axes()
        self._get_rebounds_bars(ax, converted_data)
        result.append((self._draw_statistic(ax, REBOUNDS_TITLE), REBOUNDS_TITLE))

        fig, ax = self._setup_axes()
        self._get_assists_bars(ax, converted_data)
        result.append(
            (
                self._draw_statistic(ax, ASSISTS_TURNOVERS_STEALS_TITLE),
                ASSISTS_TURNOVERS_STEALS_TITLE,
            )
        )

        fig, ax = self._setup_axes()
        self._get_fouls_bars(ax, converted_data)
        result.append((self._draw_statistic(ax, FOULS_TITLE), FOULS_TITLE))

        fig, ax = self._setup_axes()
        self._get_kpi_bars(ax, converted_data)
        result.append((self._draw_statistic(ax, KPI_TITLE), KPI_TITLE))

        logger.info("Все графики построены")
        return tuple(result)
