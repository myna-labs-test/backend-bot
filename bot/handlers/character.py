from datetime import datetime

from aiogram import Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.filters.command import Command

from bot.requests.character import get_characters, change_active_character
from bot.models.character import CharacterChange
from bot.utils.finite_state_machine import  print_canceled, print_models
from bot.utils.loader import bot

character_router = Router()


class CharacterState(StatesGroup):
    character_id = State()


@character_router.message(Command('choose'))
async def character_choose_start(msg: types.Message, state: FSMContext):
    await state.set_state(CharacterState.character_id)
    characters = await get_characters()
    await state.update_data(character_id=characters)
    await print_models(msg, state, characters, 'Available characters:')
    await bot.send_message(msg.chat.id, 'Choose id:')


@character_router.message(CharacterState.character_id)
async def character_choose_finish(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    character_change = CharacterChange(
        tg_id = msg.from_user.id,
        character_id = data['character_id'][int(msg.text)].id
    )
    await change_active_character(character_change)
    await msg.reply('Character changed')
    await state.clear()


