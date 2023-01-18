from aiohttp import ClientSession
from bot.utils.config import settings
from bot.models.character import Character, CharacterChange, CharacterShort, CharacterTextResponse
from bot.models.user import UserShort
from bot.models.message import MessageNew, MessageShort
from bot.utils.formatter import format_records_enumerated, format_dict_safe
from bot.exceptions.common import CommonException
from bot.requests.base import APICharacters, APIClient


async def get_characters() -> list[Character]:
    status, data = await APICharacters.get('/characters')
    if not status == 200:
        raise CommonException(data['message'], None)
    characters = format_records_enumerated(data, Character)
    return characters


async def change_active_character(character_change: CharacterChange) -> None:
    status, data = await APIClient.put('/user/character', params=format_dict_safe(character_change))
    if not status == 200:
        raise CommonException(data['message'], None)


async def get_active_character(user: UserShort) -> CharacterShort:
    status, data = await APIClient.get('/user/character', params=format_dict_safe(user))
    if not status == 200:
        raise CommonException(data['message'], None)
    return CharacterShort(**data)


async def get_character_text_response(message: MessageShort) -> CharacterTextResponse:
    status, data = await APICharacters.post('/character/text', params=format_dict_safe(message))
    if not status == 200:
        raise CommonException(data['message'], None)
    return CharacterTextResponse(**data)
