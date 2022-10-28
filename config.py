import os
import asyncio
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

__version__ = "v0.1"

if os.path.exists(".env"):
    load_dotenv(".env")
    

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", ".")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)

contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)
# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Modules"))
call_py = PyTgCalls(bot)

# Terms
# Privacy
# Security

hl = HNDLR[0]
start_time = time.time()

