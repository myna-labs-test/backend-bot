from bot.handlers.start import start_router
from bot.handlers.message import message_router
from bot.handlers.character import character_router
from bot.handlers.exception import exception_router
from bot.utils.loader import bot, dp
dp.include_router(start_router)
dp.include_router(character_router)
dp.include_router(message_router)
dp.include_router(exception_router)
dp.run_polling(bot, allowed_updates=dp.resolve_used_update_types())
