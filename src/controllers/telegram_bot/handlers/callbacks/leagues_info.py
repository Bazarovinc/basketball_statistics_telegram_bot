from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from src.constants import PARSE_MODE
from src.containers.use_cases import UseCasesContainer
from src.controllers.telegram_bot.states import LEAGUE_LINKS_ROUTES
from src.controllers.telegram_bot.utils import generate_cancel_button
from src.controllers.telegram_bot.utils.get_callback_query import get_callback_query
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService


@inject
async def get_fast_statistic_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    use_case: LeaguesService = Provide[UseCasesContainer.leagues_service],
) -> int:
    query = await get_callback_query(update)
    logger.info(f"Пользователь {update.effective_user.id} нажал кнопку {query.data}")
    league_info = use_case.get_league_by_id(query.data)
    await context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=league_info.fast_statistics_info.reply_message,
        reply_markup=InlineKeyboardMarkup(generate_cancel_button()),
        parse_mode=PARSE_MODE,
    )
    return LEAGUE_LINKS_ROUTES
