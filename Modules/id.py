from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from config import (bot, HNDLR, SUDO_USERS, LOGS_CHANNEL)
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["id"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["id"], prefixes=HNDLR))
async def id(client: Client, message: Message):
    if message.reply_to_message is None:
        await message.reply(f"This chat's ID is: {message.chat.id}")
    else:
        test = f"This user's ID is: {message.reply_to_message.from_user.id}\n\nThis chat's ID is: {message.chat.id}"
        await message.edit_text(test)



