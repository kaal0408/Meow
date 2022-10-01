# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 


from pytgcalls import idle
import asyncio
from pyrogram import idle
from . import (app, hl, arq, call_py)


if app:
    app.start()
print("Your Meow userbot Successfully Deployed ✅")

call_py()
idle()
