from typing import Final

# commands names
START_COMMAND_NAME: Final[str] = "start"
HELP_COMMAND_NAME: Final[str] = "help"
INFO_COMMAND_NAME: Final[str] = "info"
FAST_STATISTICS_COMMAND_NAME: Final[str] = "fast_statistics"
FAST_STATISTICS_TUTORIAL_COMMAND_NAME: Final[str] = "fast_statistics_tutorial"


START_COMMAND_INFO: Final[str] = "Запуск бота"
HELP_COMMAND_INFO: Final[str] = "Информация о командах бота"
INFO_COMMAND_INFO: Final[str] = "Информация о боте"
FAST_STATISTICS_INFO: Final[str] = "Получение графиков статистики игрока"
FAST_STATISTICS_TUTORIAL_INFO: Final[str] = "Туториал по тому, как отправить ссылку на игрока"

COMMANDS_INFO: Final[tuple[str, ...]] = (
    f"/{START_COMMAND_NAME} - {START_COMMAND_INFO}",
    f"/{HELP_COMMAND_NAME} - {HELP_COMMAND_INFO}",
    f"/{INFO_COMMAND_NAME} - {INFO_COMMAND_INFO}",
    f"/{FAST_STATISTICS_COMMAND_NAME} - {FAST_STATISTICS_INFO}",
    f"/{FAST_STATISTICS_TUTORIAL_COMMAND_NAME} - {FAST_STATISTICS_TUTORIAL_INFO}",
)

START_COMMAND_MESSAGE: Final[str] = (
    "Привет!👋\n"
    "Я бот, который покажет твою персональную статистику "
    "в виде графиков!\n"
    f"Используй команду /{HELP_COMMAND_NAME} для получения информации "
    "о моих возможностях"
)

AUTHORS: Final[tuple[str, ...]] = ("@n_bazarov",)
AUTHORS_STR: Final[str] = " ".join(AUTHORS)
INFO_COMMAND_MESSAGE: Final[str] = (
    "Данный бот является проектом с открытым исходным кодом.\n"
    "GitHub: https://github.com/Bazarovinc/baskteball_statistics_telegram_bot\n"
    f"Автор(ы) проекта: {AUTHORS_STR}"
)
FAST_STATISTICS_MESSAGE: Final[str] = (
    "Для начала выбери лигу, по которой хотел бы получить свою статистику"
)


HELP_COMMAND_MESSAGE: Final[str] = "\n".join(COMMANDS_INFO)


MLBL_FAST_STATISTICS_TUTORIAL: Final[str] = (
    "Чтобы ты смог получить статистику игрока - мне нужна ссылка на профиль игрока.\n\n"
    "Пришли подобную ссылку с профилем игрока, чью статистику ты хочешь посмотреть: "
    "https://moscow.ilovebasket.ru/players/408436?apiUrl="
    "https://reg.infobasket.su&compId=88649&lang=ru\n\n"
    "Ссылку пришли реплаем на это сообщение\n\n"
    f"Если не знаешь/не понимаешь, что делать смотри команду "
    f"/{FAST_STATISTICS_TUTORIAL_COMMAND_NAME}"
)

ABL_FAST_STATISTICS_TUTORIAL: Final[str] = (
    "Чтобы ты смог получить статистику игрока - мне нужна ссылка на профиль игрока.\n\n"
    "Пришли подобную ссылку с профилем игрока, чью статистику ты хочешь посмотреть: "
    "https://ablforpeople.com/player/76755?seasonId=48\n\n"
    "Ссылку пришли реплаем на это сообщение\n\n"
    f"Если не знаешь/не понимаешь, что делать смотри команду "
    f"/{FAST_STATISTICS_TUTORIAL_COMMAND_NAME}"
)
BCL_FAST_STATISTICS_TUTORIAL: Final[str] = (
    "Чтобы ты смог получить статистику игрока в сезоне ЛЧБ - "
    "мне нужна ссылка на профиль игрока в интересующем тебя сезоне.\n\n"
    "Пришли подобную ссылку с профилем игрока, чью статистику ты хочешь посмотреть: "
    "https://basketball.businesschampions.ru/season-29/players/5687\n\n"
    "Ссылку пришли реплаем на это сообщение\n\n"
    f"Если не знаешь/не понимаешь, что делать смотри команду "
    f"/{FAST_STATISTICS_TUTORIAL_COMMAND_NAME}"
)
FAST_STATISTICS_TUTORIAL_0_STEP: Final[str] = "1. Скопируй ссылку на профиль игрока"
FAST_STATISTICS_TUTORIAL_1_STEP: Final[str] = (
    "2. Нажми на сообщение с инструкцией " "и нажми на кнопку Reply/Ответить"
)
FAST_STATISTICS_TUTORIAL_2_STEP: Final[str] = (
    "3. Вставь скопированную ссылку на профиль игрока в текст сообщения ответа"
)

FAST_STATISTICS_TUTORIAL_COMMAND_MESSAGE: Final[str] = (
    "Для начала выбери лигу, по которой хотел бы получить инструкции"
)

FAST_STATISTICS_TUTORIAL_MESSAGE: Final[str] = (
    "После выбора лиги, по которой ты хочешь получить "
    "свою статистику, ты получишь сообщение с примером ссылки. "
    "Найди свой профиль или профиль игрока, чью статистику ты хочешь посмотреть:\n\n"
    f"{FAST_STATISTICS_TUTORIAL_0_STEP}\n{FAST_STATISTICS_TUTORIAL_1_STEP}\n"
    f"{FAST_STATISTICS_TUTORIAL_2_STEP}\n\n"
    "Ниже пришлю скриншоты действий"
)

NOT_URL_ERROR_MESSAGE: Final[str] = "К сожалению, ты прислал не URL-адрес🤦‍♂\nНачни сначала"
BAD_URL_ERROR_MESSAGE: Final[str] = (
    "К сожалению, ты прислал неверный URL-адрес😢\n"
    "Ознакомься еще раз с инструкцией и начни сначала!"
)
LEAGUE_SERVER_ERROR_MESSAGE: Final[str] = (
    "К сожалению, сайт лиги не отвечает😢\nПопробуйте, позже..."
)
WAITING_MESSAGE: Final[str] = "Ожидайте...⏳"
NOT_REPLY_MESSAGE: Final[str] = (
    "К сожалению, ты прислал ссылку не ответом на инструкцию, попробуй снова..."
)
BAD_MESSAGE_REPLY_MESSAGE: Final[str] = "К сожалению, ответил реплаем не на то сообщение"
CANCEL_BUTTON: Final[str] = "🔙Отмена"
CANCEL_BUTTON_CALLBACK: Final[str] = "back"
FAST_STATISTICS_RESULT_MESSAGE: Final[str] = "Статистика игрока {username} в лиге {league}"
