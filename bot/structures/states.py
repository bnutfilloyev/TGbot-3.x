from aiogram.filters.state import State, StatesGroup


class RegState(StatesGroup):
    fullname = State()
    phone_number = State()


class BroadcastState(StatesGroup):
    broadcast = State()
