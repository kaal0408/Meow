from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from Meow import HNDLR, LOGS_CHANNEL, SUDO_USERS, app, call_py
from Meow.Modules.helpers.admins import get_administrators


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator
