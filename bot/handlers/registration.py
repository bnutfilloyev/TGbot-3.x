from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from keyboards.common_kb import contact_kb, main_menu_kb
from structures.states import RegState
from structures.database import db

register_router = Router()


@register_router.message(RegState.fullname, ~F.text.startswith("/"))
async def input_firstname(message: types.Message, state: FSMContext):
    await state.update_data(input_fullname=message.text)
    text = "Telefon raqamingizni kiriting:"
    await message.answer(text=text, reply_markup=contact_kb())
    await state.set_state(RegState.phone_number)


@register_router.message(
    RegState.phone_number, ~F.text.startswith("/") | F.text | F.contact
)
async def input_phone(message: types.Message, state: FSMContext):
    """Enter phone number."""
    if message.contact:
        phone = message.contact.phone_number

    if message.text:
        phone = message.text

    await state.update_data(input_phone=phone)
    data = await state.get_data()
    await db.user_update(user_id=message.from_user.id, data=data)
    text = "👏 Qoyil, buni uddaladingiz! Botdan foydalanish uchun quyidagi tugmalardan foydalaning."
    await message.answer(text=text, reply_markup=main_menu_kb())
    return await state.clear()
