import re


def camel_to_snake(camel_str: str) -> str:
    """
    Функция парсинга названия из CamelCase в snake_case

    Args:
        camel_str: входная строка

    Returns:
        выходная строка
    """
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", camel_str)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def snake_to_camel(snake_str: str, first_upper: bool = True) -> str:
    """
    Функция парсинга названия из snake_case в CamelCase

    Args:
        snake_str: входная строка
        first_upper: флаг того, что первое слово должно начинаться с заглавной буквы

    Returns:
        выходная строка
    """
    components = snake_str.split("_")
    if first_upper:
        return "".join(x.title() for x in components)
    return components[0] + "".join(x.title() for x in components[1:])
