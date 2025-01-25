from telegram import BotCommand
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from src.constants import (
    FAST_STATISTICS_COMMAND_NAME,
    FAST_STATISTICS_INFO,
    FAST_STATISTICS_TUTORIAL_COMMAND_NAME,
    FAST_STATISTICS_TUTORIAL_INFO,
    HELP_COMMAND_INFO,
    HELP_COMMAND_NAME,
    INFO_COMMAND_INFO,
    INFO_COMMAND_NAME,
    START_COMMAND_INFO,
    START_COMMAND_NAME,
)
from src.constants.templates import (
    FAST_STATISTICS_LEAGUE_BUTTON_TEMPLATE,
    FAST_STATISTICS_LEAGUE_TUTORIAL_BUTTON_TEMPLATE,
)
from src.controllers.telegram_bot.handlers import (
    get_cancel_message,
    get_fast_statistic_callback,
    get_fast_statistic_tutorial_callback,
    get_fast_statistic_tutorial_keyboard,
    get_fast_statistics_keyboard,
    get_fast_statistics_result,
    get_help_message,
    get_info_message,
    get_start_message,
)
from src.controllers.telegram_bot.states import (
    LEAGUE_LINKS_ROUTES,
    START_ROUTES,
    TUTORIAL_START_ROUTES,
)

START_COMMAND_HANDLER = CommandHandler(
    START_COMMAND_NAME,
    get_start_message,
    filters=filters.ChatType.PRIVATE,
)
HELP_COMMAND_HANDLER = CommandHandler(
    HELP_COMMAND_NAME,
    get_help_message,
    filters=filters.ChatType.PRIVATE,
)
INFO_COMMAND_HANDLER = CommandHandler(
    INFO_COMMAND_NAME,
    get_info_message,
    filters=filters.ChatType.PRIVATE,
)
FAST_STATISTICS_COMMAND_HANDLER = CommandHandler(
    FAST_STATISTICS_COMMAND_NAME,
    get_fast_statistics_keyboard,
    filters=filters.ChatType.PRIVATE,
)
FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER = CommandHandler(
    FAST_STATISTICS_TUTORIAL_COMMAND_NAME,
    get_fast_statistic_tutorial_keyboard,
    filters=filters.ChatType.PRIVATE,
)
FAST_STATISTICS_QUERY_HANDLER = CallbackQueryHandler(
    get_fast_statistic_callback,
    pattern="^" + rf"{FAST_STATISTICS_LEAGUE_BUTTON_TEMPLATE}\d+" + "$",
)
FAST_STATISTICS_TUTORIAL_QUERY_HANDLER = CallbackQueryHandler(
    get_fast_statistic_tutorial_callback,
    pattern="^" + rf"{FAST_STATISTICS_LEAGUE_TUTORIAL_BUTTON_TEMPLATE}\d+" + "$",
)

FAST_STATISTICS_MESSAGE_HANDLER = MessageHandler(
    filters.ChatType.PRIVATE & filters.TEXT & (~filters.COMMAND), get_fast_statistics_result
)
BACK_QUERY_HANDLER = CallbackQueryHandler(get_cancel_message, pattern="^" + "back" + "$")


def get_command_handlers() -> tuple[CommandHandler, ...]:
    return (
        START_COMMAND_HANDLER,
        HELP_COMMAND_HANDLER,
        INFO_COMMAND_HANDLER,
        # FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER,
    )


def get_conversation_handlers() -> tuple[ConversationHandler, ...]:
    return (
        ConversationHandler(
            entry_points=[FAST_STATISTICS_COMMAND_HANDLER],
            states={
                START_ROUTES: [
                    FAST_STATISTICS_QUERY_HANDLER,
                    START_COMMAND_HANDLER,
                    HELP_COMMAND_HANDLER,
                    INFO_COMMAND_HANDLER,
                    FAST_STATISTICS_COMMAND_HANDLER,
                    FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER,
                ],
                LEAGUE_LINKS_ROUTES: [
                    FAST_STATISTICS_MESSAGE_HANDLER,
                    BACK_QUERY_HANDLER,
                    START_COMMAND_HANDLER,
                    HELP_COMMAND_HANDLER,
                    INFO_COMMAND_HANDLER,
                    FAST_STATISTICS_COMMAND_HANDLER,
                    FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER,
                ],
            },
            fallbacks=[
                BACK_QUERY_HANDLER,
            ],
        ),
        ConversationHandler(
            entry_points=[FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER],
            states={
                TUTORIAL_START_ROUTES: [
                    FAST_STATISTICS_TUTORIAL_QUERY_HANDLER,
                    START_COMMAND_HANDLER,
                    HELP_COMMAND_HANDLER,
                    INFO_COMMAND_HANDLER,
                    FAST_STATISTICS_COMMAND_HANDLER,
                    FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER,
                ],
            },
            fallbacks=[
                BACK_QUERY_HANDLER,
            ],
        ),
    )


def get_handlers() -> tuple[ConversationHandler | CommandHandler | MessageHandler, ...]:
    return get_command_handlers() + get_conversation_handlers()


async def setup_commands(application: Application) -> None:
    # set commands
    await application.bot.set_my_commands(
        (
            BotCommand(START_COMMAND_NAME, START_COMMAND_INFO),
            BotCommand(HELP_COMMAND_NAME, HELP_COMMAND_INFO),
            BotCommand(INFO_COMMAND_NAME, INFO_COMMAND_INFO),
            BotCommand(FAST_STATISTICS_COMMAND_NAME, FAST_STATISTICS_INFO),
            BotCommand(FAST_STATISTICS_TUTORIAL_COMMAND_NAME, FAST_STATISTICS_TUTORIAL_INFO),
        )
    )
