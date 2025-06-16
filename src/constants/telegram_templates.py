from typing import Final

PARSE_MODE: Final[str] = "HTML"
# commands names
START_COMMAND_NAME: Final[str] = "start"
HELP_COMMAND_NAME: Final[str] = "help"
INFO_COMMAND_NAME: Final[str] = "info"
FAST_STATISTICS_COMMAND_NAME: Final[str] = "fast_statistics"
FAST_STATISTICS_TUTORIAL_COMMAND_NAME: Final[str] = "fast_statistics_tutorial"


START_COMMAND_INFO: Final[str] = "Запуск бота и приветственное сообщение"
HELP_COMMAND_INFO: Final[str] = "Вся информация о командах бота"
INFO_COMMAND_INFO: Final[str] = "О проекте и разработчиках"
FAST_STATISTICS_INFO: Final[str] = "Получить графики статистики игрока"
FAST_STATISTICS_TUTORIAL_INFO: Final[str] = "Как отправить ссылку на игрока"

COMMANDS_INFO: Final[tuple[str, ...]] = (
    "<b>📋 Доступные команды:</b>\n\n" f"▫️/{START_COMMAND_NAME} - {START_COMMAND_INFO}",
    f"▫️/{HELP_COMMAND_NAME} - {HELP_COMMAND_INFO}",
    f"▫️/{INFO_COMMAND_NAME} - {INFO_COMMAND_INFO}",
    f"▫️/{FAST_STATISTICS_COMMAND_NAME} - {FAST_STATISTICS_INFO}",
    f"▫️/{FAST_STATISTICS_TUTORIAL_COMMAND_NAME} - {FAST_STATISTICS_TUTORIAL_INFO}",
)

START_COMMAND_MESSAGE: Final[str] = (
    "Привет!👋\n\n"
    "Я бот, который покажет твою <b>персональную статистику</b>📊 в виде графиков!\n\n"
    f"Используй команду /{HELP_COMMAND_NAME} для получения информации о моих возможностях"
)

AUTHORS: Final[tuple[str, ...]] = ("@n_bazarov",)
AUTHORS_STR: Final[str] = " ".join(AUTHORS)
INFO_COMMAND_MESSAGE: Final[str] = (
    "Данный бот является <b>проектом с открытым исходным кодом</b>.\n\n"
    "GitHub: <a href='https://github.com/Bazarovinc/baskteball_statistics_telegram_bot'>"
    "Bazarovinc/baskteball_statistics_telegram_bot</a>\n\n"
    f"<b>Автор(ы) проекта:</b> {AUTHORS_STR}"
)
FAST_STATISTICS_MESSAGE: Final[str] = "Для начала выбери лигу, по которой хотел бы получить свою статистику"


HELP_COMMAND_MESSAGE: Final[str] = "\n".join(COMMANDS_INFO)


FAST_STATISTICS_REPLY_MESSAGE: Final[str] = (
    "🏀📊<b>Чтобы получить статистику игрока, мне нужна ссылка на его профиль</b>\n\n"
    "Пришли подобную ссылку с профилем игрока, чью статистику хочешь посмотреть:\n"
    "{link}\n\n"
    "⚠️ <b>Важно:</b> Ссылку нужно прислать <i>ответом (Reply)</i> на это сообщение\n\n"
    "Если не знаешь как это сделать - используй команду "
    f"/{FAST_STATISTICS_TUTORIAL_COMMAND_NAME} для получения инструкции"
)

FAST_STATISTICS_TUTORIAL_1_STEP: Final[str] = f"1. Вызови команду → /{FAST_STATISTICS_TUTORIAL_COMMAND_NAME}"
FAST_STATISTICS_TUTORIAL_2_STEP: Final[str] = "2. Выбери лигу из предложенных вариантов"
FAST_STATISTICS_TUTORIAL_3_STEP: Final[str] = (
    "3. Найди свой профиль (или профиль нужного игрока) и скопируй ссылку на него"
)
FAST_STATISTICS_TUTORIAL_4_STEP: Final[str] = "4. Нажми на это сообщение и выбери Reply(Ответить)"
FAST_STATISTICS_TUTORIAL_5_STEP: Final[str] = "5. Вставь скопированную ссылку в ответ и отправь"

FAST_STATISTICS_TUTORIAL_COMMAND_MESSAGE: Final[str] = "Для начала выбери лигу, по которой хотел бы получить инструкции"

FAST_STATISTICS_TUTORIAL_MESSAGE: Final[str] = (
    "<b>📊 Как посмотреть статистику игрока?</b>\n"
    f"1. <b>Вызови команду</b> → /{FAST_STATISTICS_TUTORIAL_COMMAND_NAME}\n"
    "2. <b>Выбери лигу</b> из предложенных вариантов\n"
    "3. <b>Найди свой профиль</b> (или профиль нужного игрока) и <i>скопируй ссылку</i> на него\n"
    "4. <b>Нажми</b> на это сообщение и выбери <code>Reply</code> <b>(Ответить)</b>\n"
    "5. <b>Вставь скопированную ссылку</b> в ответ и отправь\n\n"
    "Ниже пришлю скриншоты действий"
)

NOT_URL_ERROR_MESSAGE: Final[str] = "К сожалению, ты прислал не URL-адрес🤦‍♂\nНачни сначала"
BAD_URL_ERROR_MESSAGE: Final[str] = (
    "К сожалению, ты прислал неверный URL-адрес😢\n" "Ознакомься еще раз с инструкцией и начни сначала!"
)
LEAGUE_SERVER_ERROR_MESSAGE: Final[str] = "К сожалению, сайт лиги не отвечает😢\nПопробуйте, позже..."
WAITING_MESSAGE: Final[str] = "Ожидайте...⏳"
NOT_REPLY_MESSAGE: Final[str] = "К сожалению, ты прислал ссылку не ответом на инструкцию, попробуй снова..."
BAD_MESSAGE_REPLY_MESSAGE: Final[str] = (
    "❌ <b>Ошибка</b>\n\n" "Кажется, ты ответил не на то сообщение. Давай попробуем еще раз😎"
)
CANCEL_BUTTON: Final[str] = "🔙Отмена"
CANCEL_BUTTON_CALLBACK: Final[str] = "back"
FAST_STATISTICS_RESULT_MESSAGE: Final[str] = "Статистика игрока {username} в лиге {league}"
