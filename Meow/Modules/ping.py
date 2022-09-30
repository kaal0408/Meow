from datetime import datetime
from pyrogram import Client
from pyrogram import filters
from Meow import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

StartTime = time.time()
owner = 'Client.first.name'

@meow_on_cmd(
    ["ping"], prefixes=HNDLR)
async def pingme(app: Client, message: Message):
    start = datetime.now()
    end = datetime.now()
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    end_time = time.time()
    m_s = (end - start).microseconds / 1000
    photo = "https://telegra.ph/file/3c2932815330a143fa1a8.png"
    await message.delete()
    if message.reply_to_message:
        await app.send_photo(
            message.chat.id,
            photo,
            caption=f"**◦•●◉✿ ᴘᴏɴɢ ✿◉●•◦**\nᴛɪᴍᴇ ᴛᴀᴋᴇɴ:`{m_s} ms`\nꜱᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ: {uptime}'\ ** ⭐MY owner → `{owner} ",
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await app.send_photo(message.chat.id, photo, caption=f"**◦•●◉✿ ᴘᴏɴɢ ✿◉●•◦**\nᴛɪᴍᴇ ᴛᴀᴋᴇɴ:`{m_s} ms`\nꜱᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ: {uptime}")
