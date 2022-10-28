

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

from config import (bot, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["kickall"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["kickall"], prefixes=HNDLR))
async def kickall(client: Client, message: Message):
    await message.reply_text("kick all chat members!")
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass




