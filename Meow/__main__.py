# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 
# Contribution by @Alone_loverboy
from pyrogram import idle
import asyncio
from . import (app as Manjeet, hl, TIMEZONE, LOGS_CHANNEL, MONGO_DB, SUDO_USERS, call_py  )
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle

if Manjeet:
    Manjeet.start()
    idle()
    call_py.start()
    pyidle()
    print("Meow Deployed Successfully✅")



