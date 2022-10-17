# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 
# Contribution by @Alone_loverboy
from pyrogram import idle
from pytgcalls import idle as pidle
import asyncio
from . import (app, app2, app3, app4, app5, hl, TIMEZONE, LOGS_CHANNEL, MONGO_DB, SUDO_USERS, call_py )

if app2:
    app2.start()
print("Your 2Client Successfully Deployed ✅")
if app3:
    app3.start()
print("Your 3Client Successfully Deployed ✅")
if app4:
    app4.start()
print("Your 4Client Successfully Deployed ✅")
if app5:
    app5.start()
print("Your 5Client Successfully Deployed ✅")

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





