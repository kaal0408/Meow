# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 
# Contribution by @Alone_loverboy
from pyrogram import idle
import asyncio
from . import (app, hl, TIMEZONE, LOGS_CHANNEL, MONGO_DB, SUDO_USERS )
from pytgcalls import idle as pyidle
from core.stream import run

app.start()
run()
idle()
print("UserBot Started")





