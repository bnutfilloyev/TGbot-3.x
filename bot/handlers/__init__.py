from handlers.common import start_router
from handlers.registration import register_router
from handlers.broadcast import broadcast_router

routers = (start_router, register_router, broadcast_router)