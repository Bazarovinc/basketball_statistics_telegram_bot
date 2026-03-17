from bs4 import BeautifulSoup, Tag

from src.constants import MATCH_TABLE_KEYS
from src.domain.dto.leagues_data.bcl.fast_statistics import BCLPlayerFastStatisticsResponseSchema


def parse_player_info(soup: BeautifulSoup) -> BCLPlayerFastStatisticsResponseSchema | None:
    """Имя и фамилия из блока .player-page__player-name (формат: «Имя Фамилия»)."""
    name_block = soup.find("div", class_="player-page__player-name")
    if not name_block:
        return None
    parts = name_block.get_text(strip=True).split()
    return BCLPlayerFastStatisticsResponseSchema(
        first_name=parts[0],
        last_name=" ".join(parts[1:]),
    )
    return None


def parse_matches_table(soup: BeautifulSoup) -> list[dict[str, str]]:
    """Таблица матчей в section.player-page-tables (заголовок «Матчи»), без tbody."""
    section = soup.find("section", class_="player-page-tables")
    if not section:
        return []
    title_div = section.find("div", class_="player-page-tables__title")
    if not title_div or "Матчи" not in title_div.get_text():
        return []
    table = section.find("table")
    if not table or not table.find("thead"):
        return []
    all_rows = table.find_all("tr")
    if len(all_rows) < 2:  # noqa: PLR2004
        return []
    data_rows = [tr for tr in all_rows if tr.get("data-match")]
    if not data_rows:
        return []
    game_statistics: list[dict[str, str]] = []
    num_stat_cells = len(MATCH_TABLE_KEYS) - 2  # Матч и F5 берём отдельно
    min_cells = 4 + num_stat_cells  # td[0]..td[3] + ячейки статистики
    for tr in data_rows:
        cells = tr.find_all("td")
        if len(cells) < min_cells:
            continue
        match_name = extract_match_name(cells[1])
        f5_value = extract_f5(cells[3])
        stat_texts = [td.get_text(strip=True) for td in cells[4 : 4 + num_stat_cells]]
        row_values = [match_name, f5_value] + stat_texts
        game_statistics.append(dict(zip(MATCH_TABLE_KEYS, row_values)))
    return game_statistics


def extract_match_name(td: Tag) -> str:
    """Из ячейки с матчем: «Команда1 - Команда2» по ссылкам .team-name a."""
    links = td.select(".team-name a")
    return " - ".join(a.get_text(strip=True) for a in links[:2])


def extract_f5(td: Tag) -> str:
    """F5: в новом HTML галочка — <i class=\"fa fa-check\">, для схемы нужен символ √."""
    if td.find(class_="fa-check"):
        return "√"
    return td.get_text(strip=True) or ""
