from typing import Final

PARSE_MODE: Final[str] = "HTML"
# commands names
START_COMMAND_NAME: Final[str] = "start"
HELP_COMMAND_NAME: Final[str] = "help"
INFO_COMMAND_NAME: Final[str] = "info"
FAST_STATISTICS_COMMAND_NAME: Final[str] = "fast_statistics"
FAST_STATISTICS_TUTORIAL_COMMAND_NAME: Final[str] = "fast_statistics_tutorial"
ADD_PROFILE_COMMAND_NAME: Final[str] = "add_profile"


START_COMMAND_INFO: Final[str] = "Запуск бота и приветственное сообщение"
HELP_COMMAND_INFO: Final[str] = "Вся информация о командах бота"
INFO_COMMAND_INFO: Final[str] = "О проекте и разработчиках"
FAST_STATISTICS_INFO: Final[str] = "Получить графики статистики игрока"
FAST_STATISTICS_TUTORIAL_INFO: Final[str] = "Как отправить ссылку на игрока"
AGREEMENT_COMMAND_NAME: Final[str] = "agreement"
AGREEMENT_COMMAND_INFO: Final[str] = "Согласие на обработку персональных данных"

DELETE_PROFILE_COMMAND_NAME: Final[str] = "delete_profile"
DELETE_PROFILE_COMMAND_INFO: Final[str] = "Удалить профиль и все данные"
ADD_PROFILE_COMMAND_INFO: Final[str] = "Сохранить профиль игрока в базу"

COMMANDS_INFO: Final[tuple[str, ...]] = (
    f"<b>📋 Доступные команды:</b>\n\n▫️/{START_COMMAND_NAME} - {START_COMMAND_INFO}",
    f"▫️/{HELP_COMMAND_NAME} - {HELP_COMMAND_INFO}",
    f"▫️/{INFO_COMMAND_NAME} - {INFO_COMMAND_INFO}",
    f"▫️/{AGREEMENT_COMMAND_NAME} - {AGREEMENT_COMMAND_INFO}",
    f"▫️/{DELETE_PROFILE_COMMAND_NAME} - {DELETE_PROFILE_COMMAND_INFO}",
    f"▫️/{FAST_STATISTICS_COMMAND_NAME} - {FAST_STATISTICS_INFO}",
    f"▫️/{FAST_STATISTICS_TUTORIAL_COMMAND_NAME} - {FAST_STATISTICS_TUTORIAL_INFO}",
    f"▫️/{ADD_PROFILE_COMMAND_NAME} - {ADD_PROFILE_COMMAND_INFO}",
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
FAST_STATISTICS_MESSAGE: Final[str] = (
    "🏀 <b>Выбери лигу для просмотра статистики</b>\n\n"
    "Чтобы получить свои данные, сначала укажи интересующую лигу из доступных вариантов:\n\n"
)
ADD_PROFILE_MESSAGE: Final[str] = (
    "🏀 <b>Выбери лигу для сохранения профиля</b>\n\nУкажи лигу, в которой хочешь сохранить свой игровой профиль:\n\n"
)
ADD_PROFILE_SUCCESS_MESSAGE: Final[str] = (
    "✅ <b>Профиль успешно сохранён</b>\n\nВаши данные по выбранной лиге сохранены в базу."
)
ADD_PROFILE_LOADING_MESSAGE: Final[str] = (
    "⏳ <b>Ожидайте</b>, загрузка и сохранение данных могут занять некоторое время…"
)
ADD_PROFILE_NOT_REPLY_MESSAGE: Final[str] = (
    "⚠️ <b>Ой, так не получится!</b>\n\n"
    "Ты прислал ссылку обычным сообщением, а не <b>ответом</b> на инструкцию.\n\n"
    f"Начни сначала 👉 /{ADD_PROFILE_COMMAND_NAME}"
)
USER_NOT_FOUND_MESSAGE: Final[str] = "❌ <b>Пользователь не найден</b>\n\nСначала запустите бота командой /start."
USER_AGREEMENT_NOT_FOUND_MESSAGE: Final[str] = (
    "❌ <b>Согласие на обработку данных не получено</b>\n\n"
    f"Используйте команду /{AGREEMENT_COMMAND_NAME} для предоставления согласия."
)
PLAYER_PROFILE_ALREADY_SAVED_MESSAGE: Final[str] = (
    "❌ <b>Профиль уже сохранён</b>\n\nВаш игровой профиль для этой лиги уже есть в базе."
)


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
    "⬇️Ниже пришлю скриншоты действий⬇️"
)

NOT_URL_ERROR_MESSAGE: Final[str] = (
    "❌ <b>Ошибка: это не ссылка!</b> 🤦‍♂\n\nПохоже, ты прислал обычный текст вместо URL-адреса"
)
BAD_URL_ERROR_MESSAGE: Final[str] = (
    "❌ <b>Ошибка: неверная ссылка!</b> 😢\n\nПрисланный URL не соответствует нужному формату"
)
LEAGUE_SERVER_ERROR_MESSAGE: Final[str] = (
    "⚠️ <b>Ошибка соединения с сайтом лиги</b> 😢\n\n"
    "К сожалению, в данный момент не удалось получить данные.\n\n"
    "<b>Пожалуйста, попробуйте позже.</b>\n\n"
    "Если проблема сохраняется, вы можете:\n"
    "• Проверить доступность сайта лиги самостоятельно\n"
    "• Попробовать другой функционал бота\n\n"
    "<i>Приносим извинения за временные неудобства!</i>"
)
WAITING_MESSAGE: Final[str] = "Ожидайте...⏳"
NOT_REPLY_MESSAGE: Final[str] = (
    "⚠️ <b>Ой, так не получится!</b>\n\n"
    "Ты прислал ссылку обычным сообщением, а не <b>ответом</b> на инструкцию.\n\n"
    f"Начни сначала 👉 /{FAST_STATISTICS_COMMAND_NAME}"
)
BAD_MESSAGE_REPLY_MESSAGE: Final[str] = (
    "❌ <b>Ошибка</b>\n\nКажется, ты ответил не на то сообщение. Давай попробуем еще раз😎"
)
CANCEL_BUTTON: Final[str] = "🔙Отмена"
CANCEL_BUTTON_CALLBACK: Final[str] = "back"

AGREEMENT_MESSAGE: Final[str] = (
    "Согласие на обработку персональных данных (152-ФЗ)\n\n"
    "Ознакомьтесь с документом и нажмите «✅ Согласен» для продолжения."
)
AGREEMENT_AGREE_BUTTON: Final[str] = "✅ Согласен"
AGREEMENT_AGREE_CALLBACK: Final[str] = "agreement_agree"
AGREEMENT_AGREED_MESSAGE: Final[str] = (
    "✅ Спасибо! Ваше согласие на обработку персональных данных принято.\n\n"
    "Теперь вам доступна вся функциональность бота."
)
AGREEMENT_ALREADY_GIVEN_MESSAGE: Final[str] = (
    "✅ Согласие на обработку персональных данных уже получено.\n\nСпасибо! Вы можете продолжить пользоваться сервисом."
)

DELETE_PROFILE_WARNING_MESSAGE: Final[str] = (
    "⚠️ <b>Удаление профиля</b>\n\n"
    "Вы уверены, что хотите удалить свой профиль?\n\n"
    "Будут безвозвратно удалены:\n"
    "• Ваши персональные данные\n"
    "• Согласие на обработку ПД\n"
    "• Вся статистика игр и привязки к лигам\n\n"
    "Это действие нельзя отменить."
)
DELETE_PROFILE_CONFIRM_BUTTON: Final[str] = "Да"
DELETE_PROFILE_CONFIRM_CALLBACK: Final[str] = "delete_profile_confirm"
DELETE_PROFILE_SUCCESS_MESSAGE: Final[str] = (
    "✅ Ваш профиль и все связанные данные удалены.\n\n"
    "Спасибо, что пользовались сервисом. Вы всегда можете начать заново командой /start."
)

FAST_STATISTICS_RESULT_MESSAGE: Final[str] = (
    "📊 <b>Статистика игрока {username} в лиге 🏀{league}</b>\n\n⬇️ <i>Ниже представлены подробные данные</i> ⬇️"
)
FAST_STATISTICS_TOTAL_TEMPLATE = """<b>{username}</b>
<code>{league} | Игр: {total_games}</code>

<b>СТАТИСТИКА ИГРОКА:</b>
<pre>
+---+---------+---------+
|   |  Всего  | За игру |
+---+---------+---------+
|О  | {total_points:>7} | {mean_total_points:>7} |
|ШБ | {total_points_1:>3}/{total_shots_1:<3} | {percent_shots_1:>6}% |
|2х | {total_points_2:>3}/{total_shots_2:<3} | {percent_shots_2:>6}% |
|3х | {total_points_3:>3}/{total_shots_3:<3} | {percent_shots_3:>6}% |
|ПБ | {total_rebounds:>7} | {mean_rebounds:>7} |
|СЩ | {total_defence_rebounds:>7} | {mean_defence_rebounds:>7} |
|ЧЩ | {total_offence_rebounds:>7} | {mean_offence_rebounds:>7} |
|ГП | {total_assists:>7} | {mean_assists:>7} |
|ПХ | {total_steals:>7} | {mean_steals:>7} |
|БШ | {total_blocks:>7} | {mean_blocks:>7} |
|ПТ | {total_turnovers:>7} | {mean_turnovers:>7} |
|Ф  | {total_fouls:>7} | {mean_fouls:>7} |
|ФС | {total_opponent_fouls:>7} | {mean_opponent_fouls:>7} |
|+/-| {total_plus_minus:>7} | {mean_plus_minus:>7} |
|KPI| {total_kpi:>7} | {mean_kpi:>7} |
|5  | {total_start:>7} |         |
|СВ | {total_played_time:>7} | {mean_played_time:>7} |
+---+---------+---------+
</pre>"""
