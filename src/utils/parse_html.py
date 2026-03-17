import re
from collections import Counter
from datetime import date, datetime

from bs4 import BeautifulSoup
from pydantic import AnyHttpUrl

from src.constants import BCL_HOST
from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.dto.leagues_data.bcl.fast_statistics import (
    BCLFastStatisticsSchema,
    BCLPlayerFastStatisticsResponseSchema,
)
from src.domain.dto.leagues_data.bcl.full_statistics import (
    BCLDivisionInfoSchema,
    BCLPlayerProfileInfoSchema,
    BCLTeamInfoSchema,
)
from src.domain.enums import PositionEnum


def parse_bcl_player_profile(soup: BeautifulSoup, player_id: str) -> BCLPlayerProfileInfoSchema:
    # Имя: полное ФИО из alt изображения или og:title
    first_name = ""
    last_name = ""
    middle_name: str | None = None

    img = soup.find("div", class_="bordered-image")
    if img:
        img_tag = img.find("img", alt=True)
        if img_tag and img_tag.get("alt"):
            full_name = img_tag["alt"].strip()
            parts = full_name.split()
            if len(parts) >= 2:
                last_name = parts[0]
                first_name = parts[1]
                middle_name = parts[2] if len(parts) >= 3 else None
    if not last_name or not first_name:
        meta_og = soup.find("meta", property="og:title")
        if meta_og and meta_og.get("content"):
            full = meta_og["content"].split(" (")[0].strip()
            parts = full.split()
            if len(parts) >= 2:
                last_name = parts[0]
                first_name = parts[1]
                middle_name = parts[2] if len(parts) >= 3 else None
    if not last_name or not first_name:
        section = soup.find("section")
        if section:
            header = section.find("header")
            if header:
                two_names = header.get_text(strip=True).split()
                if len(two_names) >= 2:
                    last_name = two_names[0]
                    first_name = two_names[1]

    # Таблица «Информация»
    info: dict[str, str] = {}
    for section in soup.find_all("section"):
        header = section.find("header")
        if header and header.get_text(strip=True) == "Информация":
            table = section.find("table", class_="values-table")
            if table:
                for tr in table.find_all("tr"):
                    th, td = tr.find("th"), tr.find("td")
                    if th and td:
                        key = th.get_text(strip=True).rstrip(":")
                        info[key] = td.get_text(strip=True)
            break

    player_height_data = info.get("Рост", "")
    player_weight_data = info.get("Вес", "")
    player_height = int(player_height_data) if player_height_data.isalnum() else None
    player_weight = int(player_weight_data) if player_weight_data.isalnum() else None

    birthdate: date | None = None
    birth_raw = info.get("Дата рождения", "").strip()
    if birth_raw and birth_raw != "-":
        try:
            birthdate = datetime.strptime(birth_raw, "%d.%m.%Y").date()
        except ValueError:
            pass

    try:
        position = PositionEnum(info.get("Амплуа", ""))
    except ValueError:
        position = None

    # Фото: относительный путь или полный URL
    photo_url: AnyHttpUrl | None = None
    photo: str | None = None
    if img:
        img_tag = img.find("img", src=True)
        if img_tag and img_tag.get("src"):
            src = img_tag["src"].strip()
            if src.startswith("http"):
                try:
                    photo_url = AnyHttpUrl(src)
                    photo = src
                except Exception:
                    pass
            else:
                base = f"https://{BCL_HOST}"
                if not src.startswith("/"):
                    base += "/"
                photo_url = AnyHttpUrl(base.rstrip("/") + "/" + src.lstrip("/"))

    return BCLPlayerProfileInfoSchema(
        profile_id=player_id,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        player_height=player_height,
        player_weight=player_weight,
        birthdate=birthdate,
        position=position,
        photo_url=photo_url,
    )


def check_player_played_in_season(soup: BeautifulSoup) -> bool:
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


def check_player_in_team(soup: BeautifulSoup, player_id: str) -> bool:
    pattern = re.compile(r"/players/" + player_id + r"(?:/|$)")
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


def parse_current_season_name(soup: BeautifulSoup) -> str:
    """Извлекает название текущего сезона из меню сезонов (#seasons-links)."""
    return (
        soup.find("nav", id="seasons-links")
        .find("div", class_="header")
        .find("span", class_="title")
        .get_text(strip=True)
    )


def parse_season_ids(soup: BeautifulSoup) -> list[int]:
    """Извлекает список season_id из меню сезонов (#seasons-links)."""
    nav = soup.find("nav", id="seasons-links")
    if not nav:
        return []

    season_ids: list[int] = []
    seen: set[int] = set()
    pattern = re.compile(r"/season-(\d+)/")

    for a in nav.find_all("a", href=True):
        href = a["href"]
        match = pattern.search(href)
        if match:
            sid = int(match.group(1))
            if sid not in seen:
                seen.add(sid)
                season_ids.append(sid)

    return sorted(season_ids, reverse=True)


def parse_fast_statistics(soup: BeautifulSoup) -> BCLFastStatisticsSchema:
    sections = soup.findAll("section")
    game_statistics: list[dict] = []
    player_info: BCLPlayerFastStatisticsResponseSchema | None = None
    games_count: int = 0
    for i, section in enumerate(sections):
        header = section.find("header")
        if header and i == 1:
            last_name, first_name = header.text.split()
            player_info = BCLPlayerFastStatisticsResponseSchema(last_name=last_name, first_name=first_name)
        if header and header.text == "Статистика":
            table = section.find("table")
            names = (th.text for th in table.find("thead").find_all("th"))
            values = (td.text for td in table.find("tbody").find_all("td"))
            stats = {key: value for key, value in zip(names, values)}
            games_count = int(stats.get("Игр"))
        if header and header.text == "Матчи":
            table = section.find("table")
            names = ((th.text for th in table.find("thead").find_all("th")) for _ in range(games_count))
            values = (td.text for td in table.find("tbody").find_all("td"))
            game_statistics = [{key: value for key, value in zip(i, values)} for i in names]
    return BCLFastStatisticsSchema(player_info=player_info, statistics_per_game=game_statistics)


def parse_team_id(player_season_page: BeautifulSoup) -> Counter:
    """Команда из блока «Матчи»: id команды с наибольшим числом появлений в матчах."""
    pattern = re.compile(r"/teams/(\d+)")
    counter: Counter[int] = Counter()
    for section in player_season_page.find_all("section"):
        header = section.find("header")
        if header and header.get_text(strip=True) != "Матчи":
            continue
        table = section.find("table")
        if not table:
            continue
        tbody = table.find("tbody")
        if not tbody:
            continue
        for tr in tbody.find_all("tr"):
            first_td = tr.find("td")
            if not first_td:
                continue
            for a in first_td.find_all("a", href=True):
                m = pattern.search(a["href"])
                if m:
                    counter[int(m.group(1))] += 1
        break
    return counter


def parse_bcl_division_and_team(
    soup: BeautifulSoup,
    season_id: str,
    external_team_id: str,
) -> BCLDivisionInfoSchema:
    division_name = ""
    for section in soup.find_all("section"):
        header = section.find("header")
        if header and header.get_text(strip=True) == "Турнирная таблица":
            article = section.find("article")
            if article:
                art_header = article.find("header")
                if art_header:
                    division_name = art_header.get_text(strip=True)
            break

    external_division_id = f"{division_name}_{season_id}" if division_name else f"unknown_{season_id}"

    team_name = ""
    logo_url: AnyHttpUrl | None = None

    # Название команды — в правой колонке, в заголовке секции с описанием команды
    right_col = soup.find("div", class_="right w750")
    if right_col:
        first_section = right_col.find("section")
        if first_section:
            h = first_section.find("header")
            if h:
                team_name = h.get_text(strip=True)

    for section in soup.find_all("section"):
        header = section.find("header")
        if header and header.get_text(strip=True) == "Турнирная таблица":
            prev = section.find_previous_sibling("section")
            if prev:
                photo_block = prev.find("div", class_="photo-block")
                if photo_block:
                    img = photo_block.find("img", src=True)
                    if img and img.get("src"):
                        src = img["src"].strip()
                        if src.startswith("http"):
                            try:
                                logo_url = AnyHttpUrl(src)
                            except Exception:
                                pass
                        else:
                            base = f"https://{BCL_HOST}"
                            if not src.startswith("/"):
                                base += "/"
                            try:
                                logo_url = AnyHttpUrl(base.rstrip("/") + "/" + src.lstrip("/"))
                            except Exception:
                                pass
            break

    team = BCLTeamInfoSchema(
        external_team_id=external_team_id,
        team_name=team_name or "Unknown",
        league=LeagueTypeEnum.BCL,
        logo_url=logo_url,
    )
    return BCLDivisionInfoSchema(
        external_division_id=external_division_id,
        name=division_name or "Unknown",
        league=LeagueTypeEnum.BCL,
        teams=[team],
    )


def parse_bcl_team_game_ids(soup: BeautifulSoup) -> list[str]:
    seen: set[str] = set()
    game_ids: list[str] = []
    pattern = re.compile(r"/matches/(\d+)")
    for section in soup.find_all("section"):
        header = section.find("header")
        if header and header.get_text(strip=True) != "Расписание":
            continue
        for a in section.find_all("a", href=True):
            match = pattern.search(a["href"])
            if match:
                gid = match.group(1)
                if gid not in seen:
                    seen.add(gid)
                    game_ids.append(gid)
        break
    return game_ids
