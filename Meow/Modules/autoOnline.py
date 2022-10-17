import asyncio
from pyrogram import Client, filters
from pyrogram.types import *
from Meow import (app, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["online"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["online"], prefixes=HNDLR))
async def online_now(client: Client, message: Message):
    await message.edit("AutoOnline activated")
    while True:
        iii = await client.send_message("me", "bruh")
        await client.delete_messages("me", iii.id)
        await asyncio.sleep(45)


