# hehehe Not for you
# (c) @Alone_loverboy || (https://DevAdarsh.me/)

#Soo lets start
import os
from pyrogram import Client 
from pytgcalls import PyTgCalls 
from . import (SESSION, API_ID, API_HASH)

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
SESSION = os.environ.get("SESSION", "")

app = Client(
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': 'Meow.Modules'}
)


print("Connected to Client.")
