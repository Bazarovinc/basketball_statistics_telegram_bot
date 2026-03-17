import re

from bs4 import BeautifulSoup

from src.domain.dto.leagues_data.bcl.player_profile import BCLPlayerProfilePageSchema
from src.domain.use_cases.parsers.bcl_parser import BCLParser


def bcl_team_page_has_player(soup: BeautifulSoup, player_id: int) -> bool:
    """
    Проверяет, есть ли игрок с указанным player_id в составе команды на странице команды BCL.
    Принимает объект BeautifulSoup страницы команды (например, /season-31/teams/72)
    и player_id. Возвращает True, если ссылка на этого игрока найдена в блоке состава/игроков.
    """
    pattern = re.compile(r"/players/" + str(player_id) + r"(?:/|$)")
    for section in soup.find_all("section"):
        header = section.find("header")
        if header is None:
            continue
        title = header.get_text(strip=True)
        # Состав команды и таблица «Игроки» — блоки, где перечислены игроки
        if "Состав" not in title and "Игроки" not in title:
            continue
        for a in section.find_all("a", href=True):
            if pattern.search(a["href"]):
                return True
    # Дополнительно проверяем таблицы с классом (таблица «Игроки» может быть не в section)
    for table in soup.find_all("table"):
        for a in table.find_all("a", href=True):
            if pattern.search(a["href"]):
                return True
    return False


def bcl_player_played_in_season(soup: BeautifulSoup) -> bool:
    """
    Определяет, играл ли игрок в сезоне (есть хотя бы одна игра).
    Принимает объект BeautifulSoup страницы профиля игрока BCL.
    Возвращает True, если игрок играл; False, если не играл (нет ни одной игры).
    """
    for section in soup.find_all("section"):
        header = section.find("header")
        if header and header.get_text(strip=True) == "Статистика":
            table = section.find("table")
            if not table or not table.find("thead") or not table.find("tbody"):
                return False
            thead = table.find("thead")
            tbody = table.find("tbody")
            names = [th.get_text(strip=True) for th in thead.find_all("th")]
            values = [td.get_text(strip=True) for td in tbody.find_all("td")]
            if not names or not values:
                return False
            stats = dict(zip(names, values))
            games_str = stats.get("Игр", "0")
            try:
                return int(games_str) > 0
            except ValueError:
                return False
    return False


def parse_bcl_player_profile_page(html: str) -> BCLPlayerProfilePageSchema:
    """
    Парсит HTML страницы профиля игрока BCL.
    Извлекает team_id (команда игрока) и season_ids (доступные сезоны).
    """
    soup = BeautifulSoup(html, "html.parser")

    team_id = BCLParser._parse_team_id(soup)
    season_ids = BCLParser._parse_season_ids(soup)

    return BCLPlayerProfilePageSchema(team_id=team_id, season_ids=season_ids)
