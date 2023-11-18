import asyncio
import logging

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError, TelegramNotFound, TelegramRetryAfter, TelegramAPIError


async def copy_message(
    user_id: str, chat_id: int, message_id: int, keyboard: InlineKeyboardMarkup, bot: Bot
) -> bool:
    """
    Safe messages sender
    :param user_id:
    :param chat_id:
    :param message_id:
    :param keyboard: Inline keyboard for post
    :return:
    """
    try:
        await bot.copy_message(user_id, chat_id, message_id, reply_markup=keyboard)
    except TelegramForbiddenError:
        logging.info(f"Target [ID:{user_id}]: blocked by user")
    except TelegramNotFound:
        logging.info(f"Target [ID:{user_id}]: invalid user ID")
    except TelegramRetryAfter as e:
        logging.info(
            f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds."
        )
        await asyncio.sleep(e.timeout)
        return await copy_message(
            user_id, chat_id, message_id, keyboard
        )  # Recursive call
    except TelegramAPIError:
        logging.info(f"Target [ID:{user_id}]: failed")
    else:
        logging.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def send_message(
        user_id: int, text: str,  keyboard: InlineKeyboardMarkup | ReplyKeyboardMarkup, bot: Bot
        ) -> bool:
    """
    Safe messages sender
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_message(user_id, text, reply_markup=keyboard)
    except TelegramForbiddenError:
        logging.error(f"Target [ID:{user_id}]: blocked by user")
    except TelegramNotFound:
        logging.error(f"Target [ID:{user_id}]: invalid user ID")
    except TelegramRetryAfter as e:
        logging.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text)  # Recursive call
    except TelegramAPIError:
        logging.exception(f"Target [ID:{user_id}]: failed")
    else:
        logging.info(f"Target [ID:{user_id}]: success")
        return True
    return False

async def send_photo(
        user_id: int, photo: str, caption: str, keyboard: InlineKeyboardMarkup | ReplyKeyboardMarkup, bot: Bot
        ) -> bool:
    """
    Safe messages sender
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_photo(user_id, photo, caption=caption, reply_markup=keyboard)
    except TelegramForbiddenError:
        logging.error(f"Target [ID:{user_id}]: blocked by user")
    except TelegramNotFound:
        logging.error(f"Target [ID:{user_id}]: invalid user ID")
    except TelegramRetryAfter as e:
        logging.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_photo(user_id, photo, caption, keyboard)
    except TelegramAPIError:
        logging.exception(f"Target [ID:{user_id}]: failed")
    else:
        logging.info(f"Target [ID:{user_id}]: success")
        return True
    return False
