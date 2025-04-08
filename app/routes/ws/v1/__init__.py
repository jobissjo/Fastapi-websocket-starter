from fastapi import APIRouter
from app.routes.ws.v1 import chat_ws

router = APIRouter(prefix="/v1/ws")
router.include_router(chat_ws.router)
