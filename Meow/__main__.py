# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 
# Contribution by @Alone_loverboy
from pyrogram import idle
import asyncio
from . import (app, hl, TIMEZONE, LOGS_CHANNEL, MONGO_DB, SUDO_USERS )

app.start()
app.send_message(LOGS_CHANNEL, Meow is deploy successfully)
idle()
print("UserBot Started")





