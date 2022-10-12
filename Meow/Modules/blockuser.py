from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from Meow import (app, app2, app3, app4, app5, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["block"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["block"], prefixes=HNDLR))
async def block_user(client: Client, message: Message):
    if not message.chat.type == "private":
        await message.reply("Can't block the group LOL !")
    else:
        user_id=message.chat.id
        await message.edit("You have been blocked succesfully due to your sins !!")
        await client.block_user(int(user_id))


