from aiogram import Router


def setup_routers() -> Router:
    from . import test

    router = Router()
    router.include_router(test.router)

    return router
