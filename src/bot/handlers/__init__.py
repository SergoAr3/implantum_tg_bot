from aiogram import Router

from bot.handlers.appointment import router as appointment_router
from bot.handlers.common import router as common_router


def setup_routers() -> Router:
    router = Router(name="root")
    router.include_routers(common_router, appointment_router)
    return router

