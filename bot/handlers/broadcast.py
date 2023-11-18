from aiogram import Router, types, Bot
from structures.states import BroadcastState
from structures.database import db
from structures.broadcaster import copy_message
from aiogram.fsm.context import FSMContext


broadcast_router = Router()


@broadcast_router.message(BroadcastState.broadcast)
async def broadcast_command(message: types.Message, state: FSMContext, bot: Bot):
    """Broadcast command."""
    text = message.text
    sended = blocked = 0
    await message.answer(text=f"🚀 Xabar yuborilmoqda...")
    for user in await db.users_list():
        is_sended = await copy_message(
            user_id=user["user_id"],
            chat_id=message.chat.id,
            message_id=message.message_id,
            keyboard=message.reply_markup,
            bot=bot,
        )
        if not is_sended:
            blocked += 1
        else:
            sended += 1

    text = (
        f"<b>Xabar muvaffaqiyatli yuborildi!</b>\n\n"
        f"<b>🟢 Yuborilganlar soni:</b> {sended}\n"
        f"<b>🔴 Yuborilmaganlar soni:</b> {blocked}"
    )
    await message.answer(text=text)
    return await state.clear()
