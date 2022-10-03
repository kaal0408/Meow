# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang Bitch -! 

import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters


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

LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)

    
HNDLR = os.getenv("HNDLR", ".")
sudo = os.getenv("SUDO_USERS")

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)





# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------



app = Client(
    name="[Meow]",
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': 'Meow.Modules'}
)





hl = HNDLR[0]
start_time = time.time()

#-------------------------CLIENTS-----------------------------



