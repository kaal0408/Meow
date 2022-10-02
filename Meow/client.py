# hehehe Not for you
# (c) @Alone_loverboy || (https://DevAdarsh.me/)

#Soo lets start

from pyrogram import Client 
from pytgcalls import PyTgCalls 


app = Client(
    name = "[Meow😸]",
    session_name=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={"root": "Meow.Modules"}
)

callMe = PyTgCalls(app)
