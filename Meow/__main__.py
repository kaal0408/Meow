from pyrogram import idle
from pyrogram import Client as Bot
from Meow.clientbot import run
from Meow.config import API_ID, API_HASH, BOT_TOKEN
from . import meow, hl
    
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Meow.plugins")
)

if meow:
    meow.start()

bot.start()
run()
idle()
