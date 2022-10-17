# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 
# Contribution by @Alone_loverboy
from pyrogram import idle
from pytgcalls import idle as pidle
import asyncio
from . import (app, hl, TIMEZONE, LOGS_CHANNEL, MONGO_DB, SUDO_USERS, call_py )


async def main():
    print("STARTING  CLIENT")
    await app.start()
    print("STARTING PYTGCALLS CLIENT")
    await call_py.start()
    print(
        """
    ------------------------
   | Meow Actived! |
    ------------------------
"""
    )
    await idle()
    await pidle()
    print("STOPPING USERBOT")
    await app.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())





