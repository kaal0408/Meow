# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang Bitch -! 

import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls


if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.1"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
SESSION = os.getenv("SESSION", None)
TIMEZONE = os.environ.get("TIMEZONE", "Asia/Kolkata")
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)
MONGO_DB = os.environ.get("MONGO_DB", "")
    
HNDLR = os.getenv("HNDLR", ".")
sudo = os.getenv("SUDO_USERS")

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)

contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)


# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------


if SESSION:
   app = Client(
    name="[Meow]",
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': 'Meow.Modules'}
)
   print("Client 1 Found")
else: 
   app = none

call_py = PyTgCalls(app)






hl = HNDLR[0]
start_time = time.time()

#-------------------------CLIENTS-----------------------------



