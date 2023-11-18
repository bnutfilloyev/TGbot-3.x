from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from keyboards.common_kb import contact_kb, main_menu_kb, remove_kb
from structures.database import db
from structures.states import RegState, BroadcastState

start_router = Router()


@start_router.message(Command("start"))
async def start_command(
    message: types.Message, state: FSMContext, command: CommandObject
):
    """Start command."""
    user_data = {
        "username": message.from_user.username,
        "fullname": message.from_user.full_name,
    }

    user_info = await db.user_update(user_id=message.from_user.id, data=user_data)

    if user_info.get("input_fullname") is None:
        text = "Botdan foydalanish uchun avval ro'yxatdan o'tishingiz kerak. Iltimos, ism familiyangizni kiriting:"
        await message.answer(text=text, reply_markup=remove_kb())
        return await state.set_state(RegState.fullname)

    if user_info.get("input_phone") is None:
        text = "Iltimos, telefon raqamingizni kiriting:"
        await message.answer(text=text, reply_markup=contact_kb())
        return await state.set_state(RegState.phone_number)

    text = "😊 Sizni yana ko'rib turganimizdan xursandmiz! Botdan foydalanish uchun tugmalardan foydalaning!"
    await message.answer(text=text, reply_markup=main_menu_kb())


@start_router.message(Command("help"))
async def help_command(message: types.Message, state: FSMContext):
    """Help command."""
    text = "🆘 Yordam"
    await message.answer(text=text, reply_markup=main_menu_kb())
    return await state.clear()


@start_router.message(Command("broadcast"))
async def broadcast_command(message: types.Message, state: FSMContext):
    text = "Xabar matnini kiriting:"
    await message.answer(text=text)
    return await state.set_state(BroadcastState.broadcast)
