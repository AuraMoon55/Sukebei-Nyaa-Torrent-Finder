from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from bot import AUTH_CHAT

def sudo_chat_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.chat.id == AUTH_CHAT:
            return await func(client, message)

    return decorator
