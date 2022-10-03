# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 
# Contribution by @Alone_loverboy
from pyrogram import idle
import asyncio
from . import (app, hl, TIMEZONE, LOGS_CHANNEL, MONGO_DB )

if app:
    app.start()
    idle()
    print("Meow Deployed Successfully✅")

print('Deployed')
