# hehehe Not for you
# (c) @Alone_loverboy || (https://DevAdarsh.me/)

#Soo lets start

from pyrogram import Client 
from pytgcalls import PyTgCalls 
from . import (SESSION, API_ID, API_HASH)


app = Client(name="Meow", api_id = API_ID, api_hash = API_HASH, session_string=SESSION, plugins=dict(root="Meow.Modules"))
print("Client  Found")


callMe = PyTgCalls(app)
