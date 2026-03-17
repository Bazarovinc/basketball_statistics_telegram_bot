from telegram import BotCommand
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ConversationHandler, MessageHandler, filters

from src.constants import (
    ADD_PROFILE_COMMAND_INFO,
    ADD_PROFILE_COMMAND_NAME,
    AGREEMENT_AGREE_CALLBACK,
    AGREEMENT_COMMAND_INFO,
    AGREEMENT_COMMAND_NAME,
    DELETE_PROFILE_COMMAND_INFO,
    DELETE_PROFILE_COMMAND_NAME,
    DELETE_PROFILE_CONFIRM_CALLBACK,
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
    ADD_PROFILE_LEAGUE_BUTTON_TEMPLATE,
    FAST_STATISTICS_LEAGUE_BUTTON_TEMPLATE,
    FAST_STATISTICS_LEAGUE_TUTORIAL_BUTTON_TEMPLATE,
)
from src.controllers.telegram_bot.handlers import (
    get_add_profile_callback,
    get_add_profile_keyboard,
    get_add_profile_result,
    get_agreement_agree_callback,
    get_agreement_keyboard,
    get_cancel_message,
    get_delete_profile_confirm_callback,
    get_delete_profile_keyboard,
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
    ADD_PROFILE_LEAGUE_LINKS_ROUTES,
    ADD_PROFILE_START_ROUTES,
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
AGREEMENT_COMMAND_HANDLER = CommandHandler(
    AGREEMENT_COMMAND_NAME,
    get_agreement_keyboard,
    filters=filters.ChatType.PRIVATE,
)
AGREEMENT_QUERY_HANDLER = CallbackQueryHandler(
    get_agreement_agree_callback,
    pattern="^" + AGREEMENT_AGREE_CALLBACK + "$",
)
DELETE_PROFILE_COMMAND_HANDLER = CommandHandler(
    DELETE_PROFILE_COMMAND_NAME,
    get_delete_profile_keyboard,
    filters=filters.ChatType.PRIVATE,
)
DELETE_PROFILE_QUERY_HANDLER = CallbackQueryHandler(
    get_delete_profile_confirm_callback,
    pattern="^" + DELETE_PROFILE_CONFIRM_CALLBACK + "$",
)
ADD_PROFILE_COMMAND_HANDLER = CommandHandler(
    ADD_PROFILE_COMMAND_NAME,
    get_add_profile_keyboard,
    filters=filters.ChatType.PRIVATE,
)
ADD_PROFILE_QUERY_HANDLER = CallbackQueryHandler(
    get_add_profile_callback,
    pattern="^" + rf"{ADD_PROFILE_LEAGUE_BUTTON_TEMPLATE}\d+" + "$",
)
ADD_PROFILE_MESSAGE_HANDLER = MessageHandler(
    filters.ChatType.PRIVATE & filters.TEXT & (~filters.COMMAND), get_add_profile_result
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
        AGREEMENT_COMMAND_HANDLER,
        DELETE_PROFILE_COMMAND_HANDLER,
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
                    ADD_PROFILE_COMMAND_HANDLER,
                ],
                LEAGUE_LINKS_ROUTES: [
                    FAST_STATISTICS_MESSAGE_HANDLER,
                    BACK_QUERY_HANDLER,
                    START_COMMAND_HANDLER,
                    HELP_COMMAND_HANDLER,
                    INFO_COMMAND_HANDLER,
                    FAST_STATISTICS_COMMAND_HANDLER,
                    FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER,
                    ADD_PROFILE_COMMAND_HANDLER,
                ],
            },
            fallbacks=[
                BACK_QUERY_HANDLER,
            ],
        ),
        ConversationHandler(
            entry_points=[ADD_PROFILE_COMMAND_HANDLER],
            states={
                ADD_PROFILE_START_ROUTES: [
                    ADD_PROFILE_QUERY_HANDLER,
                    BACK_QUERY_HANDLER,
                    START_COMMAND_HANDLER,
                    HELP_COMMAND_HANDLER,
                    INFO_COMMAND_HANDLER,
                    FAST_STATISTICS_COMMAND_HANDLER,
                    FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER,
                    ADD_PROFILE_COMMAND_HANDLER,
                ],
                ADD_PROFILE_LEAGUE_LINKS_ROUTES: [
                    ADD_PROFILE_MESSAGE_HANDLER,
                    BACK_QUERY_HANDLER,
                    START_COMMAND_HANDLER,
                    HELP_COMMAND_HANDLER,
                    INFO_COMMAND_HANDLER,
                    FAST_STATISTICS_COMMAND_HANDLER,
                    FAST_STATISTICS_TUTORIAL_COMMAND_HANDLER,
                    ADD_PROFILE_COMMAND_HANDLER,
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
                    ADD_PROFILE_COMMAND_HANDLER,
                ],
            },
            fallbacks=[
                BACK_QUERY_HANDLER,
            ],
        ),
    )


def get_handlers() -> tuple[ConversationHandler | CommandHandler | MessageHandler | CallbackQueryHandler, ...]:
    return (
        get_command_handlers() + (AGREEMENT_QUERY_HANDLER, DELETE_PROFILE_QUERY_HANDLER) + get_conversation_handlers()
    )


async def setup_commands(application: Application) -> None:
    # set commands
    await application.bot.set_my_commands(
        (
            BotCommand(START_COMMAND_NAME, START_COMMAND_INFO),
            BotCommand(HELP_COMMAND_NAME, HELP_COMMAND_INFO),
            BotCommand(INFO_COMMAND_NAME, INFO_COMMAND_INFO),
            BotCommand(AGREEMENT_COMMAND_NAME, AGREEMENT_COMMAND_INFO),
            BotCommand(DELETE_PROFILE_COMMAND_NAME, DELETE_PROFILE_COMMAND_INFO),
            BotCommand(FAST_STATISTICS_COMMAND_NAME, FAST_STATISTICS_INFO),
            BotCommand(FAST_STATISTICS_TUTORIAL_COMMAND_NAME, FAST_STATISTICS_TUTORIAL_INFO),
            BotCommand(ADD_PROFILE_COMMAND_NAME, ADD_PROFILE_COMMAND_INFO),
        )
    )
