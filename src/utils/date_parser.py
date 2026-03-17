import re
from datetime import datetime
from zoneinfo import ZoneInfo


def parse_date_from_timestamp(value: str) -> datetime:
    if matched := re.findall(r"\d+", value):
        return datetime.fromtimestamp(int(matched[0]) / 1000, tz=ZoneInfo("Europe/Moscow"))
    else:
        raise ValueError("Не найдено число для получения даты")
