 
from pyrogram import *
from pyrogram.types import *
from helpers.basic import edit_or_reply
 
import asyncio
 
from Meow import (app, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["cute"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["cute"], prefixes=HNDLR))
async def hello_world(client: Client, message: Message):
    mg = await message.edit("𝙲𝚄𝚃𝙴")
    await asyncio.sleep(0.2)
    await mg.edit("𝙲𝚄𝚃𝙴 𝙲𝚄𝚃𝙴")
    await asyncio.sleep(0.2)
    await mg.edit("𝙲𝚄𝚃𝙴 𝙲𝚄𝚃𝙴 𝙲𝚄𝚃𝙴")
    await asyncio.sleep(0.2) 
    await mg.edit("𝙲𝚄𝚃𝙴 𝙲𝚄𝚃𝙴 𝙲𝚄𝚃𝙴 𝙲𝚄𝚃𝙴")
    await asyncio.sleep(0.2) 
    await mg.edit("𝚂𝙾 𝙲𝚄𝚃𝙴")
    await asyncio.sleep(0.2) 
    await mg.edit("𝚂𝙾 𝚂𝙾 𝙲𝚄𝚃𝙴 𝙲𝚄𝚃𝙴") 
    await asyncio.sleep(0.2) 
    await mg.edit("𝙰𝙽𝙳") 
    await asyncio.sleep(0.2) 
    await mg.edit("𝙾𝙽𝙻𝚈 𝙲𝚄𝚃𝙴 𝚂𝙾 𝙲𝚄𝚃𝙴")


