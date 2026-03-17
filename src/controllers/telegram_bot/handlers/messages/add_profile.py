from dependency_injector.wiring import Provide, inject
from loguru import logger
from pydantic import AnyHttpUrl, ValidationError
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from src.constants import (
    ADD_PROFILE_LOADING_MESSAGE,
    ADD_PROFILE_NOT_REPLY_MESSAGE,
    ADD_PROFILE_SUCCESS_MESSAGE,
    BAD_MESSAGE_REPLY_MESSAGE,
    BAD_URL_ERROR_MESSAGE,
    LEAGUE_SERVER_ERROR_MESSAGE,
    NOT_URL_ERROR_MESSAGE,
    PARSE_MODE,
    PLAYER_PROFILE_ALREADY_SAVED_MESSAGE,
    USER_AGREEMENT_NOT_FOUND_MESSAGE,
    USER_NOT_FOUND_MESSAGE,
)
from src.containers.app import UseCasesContainer
from src.core.exceptions.parsers_exceptions import ServerNotAvailableException, URLValidationException
from src.core.exceptions.use_case_exceptions import (
    PlayerProfileAlreadySavedError,
    UserAgreementNotFoundError,
    UserNotFoundError,
)
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.use_cases.core_use_cases.full_statistics_saver import FullStatisticsSaver
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService


@inject
async def get_add_profile_result(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    use_case: FullStatisticsSaver = Provide[UseCasesContainer.full_statistics_saver],
    leagues_service: LeaguesService = Provide[UseCasesContainer.leagues_service],
) -> int:
    user_id = update.effective_user.id
    if not update.message.reply_to_message:
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=ADD_PROFILE_NOT_REPLY_MESSAGE,
            parse_mode=PARSE_MODE,
        )
        return ConversationHandler.END
    logger.info(f"Сообщение-ссылка для add_profile от пользователя {user_id}")
    try:
        data_from_user = AnyHttpUrl(update.effective_message.text)
    except ValidationError:
        logger.error(f"Пользователь {user_id} прислал не ссылку")
        await context.bot.send_message(update.effective_message.chat_id, text=NOT_URL_ERROR_MESSAGE)
        return ConversationHandler.END
    league_type = leagues_service.get_league_type_by_fast_statistics(update.message.reply_to_message.text)
    if not league_type:
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=BAD_MESSAGE_REPLY_MESSAGE,
            parse_mode=PARSE_MODE,
        )

        return ConversationHandler.END
    await context.bot.send_message(
        update.effective_message.chat_id,
        text=ADD_PROFILE_LOADING_MESSAGE,
        parse_mode=PARSE_MODE,
    )
    try:
        await use_case(LeagueUrlsUserInputSchema(player_url=data_from_user, league_type=league_type), tg_id=user_id)
    except URLValidationException as url_validation_error:
        logger.error(url_validation_error)
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=BAD_URL_ERROR_MESSAGE,
            parse_mode=PARSE_MODE,
        )
        return ConversationHandler.END
    except ServerNotAvailableException as server_error:
        logger.error(server_error)
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=LEAGUE_SERVER_ERROR_MESSAGE,
            parse_mode=PARSE_MODE,
        )

        return ConversationHandler.END
    except UserNotFoundError:
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=USER_NOT_FOUND_MESSAGE,
            parse_mode=PARSE_MODE,
        )
        return ConversationHandler.END
    except UserAgreementNotFoundError:
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=USER_AGREEMENT_NOT_FOUND_MESSAGE,
            parse_mode=PARSE_MODE,
        )
        return ConversationHandler.END
    except PlayerProfileAlreadySavedError:
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=PLAYER_PROFILE_ALREADY_SAVED_MESSAGE,
            parse_mode=PARSE_MODE,
        )
        return ConversationHandler.END
    await context.bot.send_message(
        update.effective_message.chat_id,
        text=ADD_PROFILE_SUCCESS_MESSAGE,
        parse_mode=PARSE_MODE,
    )
    return ConversationHandler.END
