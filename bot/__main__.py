from bot.handlers.anonymous import anonymous_router
from bot.handlers.group import group_router
from bot.handlers.homeworks import homework_router
from bot.handlers.start import start_router
from bot.utils.loader import bot, dp

dp.include_router(anonymous_router)
dp.include_router(group_router)
dp.include_router(homework_router)
dp.include_router(start_router)
dp.run_polling(bot, allowed_updates=dp.resolve_used_update_types())
