import os
from pyrogram.types import Message
from Meow import (app, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters

@app.on_message(filters.user(SUDO_USERS) & filters.command(["clean"], prefixes=HNDLR))
@app.on_message(filters.me & filters.command(["clean"], prefixes=HNDLR))
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **Ƈɭɘɑɳɘɗ**")
    else:
        await message.reply_text("✅ **Ʌɭɤɘɑɗy Ƈɭɘɑɳɘɗ**")
