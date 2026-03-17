from enum import IntEnum, StrEnum

from aenum import MultiValueEnum


class MLBLGenderEnum(IntEnum):
    male = 1
    female = 2


class PositionEnum(IntEnum, MultiValueEnum):
    point_guard = 1, "PG", "Point guard", "Разыгрывающий", "point_guard"
    shooting_guard = 2, "SG", "Shooting guard", "Атакующий защитник", "shooting_guard"
    small_forward = 3, "SF", "Small forward", "Легкий форвард", "small_forward"
    power_forward = 4, "PF", "Power forward", "Тяжелый форвард", "power_forward"
    center = 5, "C", "Center", "Центровой", "center"


class MLBLGameStatusEnum(IntEnum):
    not_finished = 0
    finished = 1


class PlayerGenderEnum(StrEnum):
    """Для отображения пользователю (М/Ж)."""

    male = "М"
    female = "Ж"


class GenderEnum(StrEnum):
    """Значения в БД (таблица user_info): gender_enum ('male', 'female')."""

    male = "male"
    female = "female"


class TeamPositionEnum(StrEnum):
    left = "left"
    right = "right"


class GameStatusEnum(StrEnum):
    scheduled = "scheduled"
    live = "live"
    finished = "finished"


class GameQuarterEnum(StrEnum):
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"
    OT1 = "OT1"
    OT2 = "OT2"
    OT3 = "OT3"
    OT4 = "OT4"
    OT5 = "OT5"
    OT6 = "OT6"
