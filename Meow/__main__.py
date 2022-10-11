# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 
# Contribution by @Alone_loverboy
from pyrogram import idle
import asyncio
from . import (app, app2, app3, app4, app5, hl, TIMEZONE, LOGS_CHANNEL, MONGO_DB, SUDO_USERS )

if app:
    app.start()
print("Your 1Client Successfully Deployed ✅")
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

idle()



