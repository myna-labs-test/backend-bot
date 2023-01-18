from aiohttp import ClientSession
from bot.configs.get_settings import get_backend_settings
from bot.models.character import Character, CharacterChange, CharacterShort, CharacterTextResponse
from bot.models.user import UserShort
from bot.models.message import MessageNew, MessageShort
from bot.utils.formatter import format_records_enumerated, format_dict_safe
from bot.exceptions.common import CommonException


async def get_characters() -> list[Character]:
    settings = get_backend_settings()
    url = f"http://{settings.BACKEND_CHARACTER_HOSTNAME}:{settings.BACKEND_CHARACTER_PORT}/characters"
    async with ClientSession() as session:
        async with session.get(url) as response:
            if not response.status == 200:
                raise CommonException((await response.json())['message'], None)
            data = await response.json()
            characters = format_records_enumerated(data,Character)
            return characters


async def change_active_character(character_change: CharacterChange) -> None:
    settings = get_backend_settings()
    url = f"http://{settings.BACKEND_CLIENT_HOSTNAME}:{settings.BACKEND_CLIENT_PORT}/user/character"
    async with ClientSession() as session:
        async with session.put(url, params=format_dict_safe(character_change)) as response:
            if not response.status == 200:
                raise CommonException((await response.json())['message'], None)


async def get_active_character(user: UserShort) -> CharacterShort:
    settings = get_backend_settings()
    url = f"http://{settings.BACKEND_CLIENT_HOSTNAME}:{settings.BACKEND_CLIENT_PORT}/user/character"
    async with ClientSession() as session:
        async with session.get(url, params=format_dict_safe(user)) as response:
            if not response.status == 200:
                raise CommonException((await response.json())['message'], None)
            data = await response.json()
            return CharacterShort(**data)


async def get_character_text_response(message: MessageShort) -> CharacterTextResponse:
    settings = get_backend_settings()
    url = f"http://{settings.BACKEND_CHARACTER_HOSTNAME}:{settings.BACKEND_CHARACTER_PORT}/character/text"
    async with ClientSession() as session:
        async with session.post(url, params=format_dict_safe(message)) as response:
            if not response.status == 200:
                raise CommonException((await response.json())['message'], None)
            data = await response.json()
            return CharacterTextResponse(**data)
