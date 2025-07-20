from enum import Enum

from aenum import MultiValueEnum


class MLBLGenderEnum(Enum):
    male = 1
    female = 2


class PositionEnum(MultiValueEnum):
    point_guard = 1, "PG", "Point guard", "Разыгрывающий"
    shooting_guard = 2, "SG", "Shooting guard", "Атакующий защитник"
    small_forward = 3, "SF", "Small forward", "Легкий форвард"
    power_forward = 4, "PF", "Power forward", "Тяжелый форвард"
    center = 5, "C", "Center", "Центровой"


class MLBLGameStatusEnum(Enum):
    not_finished = 0
    finished = 1


class PlayerGenderEnum(Enum):
    male = "М"
    female = "Ж"
