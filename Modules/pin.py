from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from config import (bot, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["pin"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["pin"], prefixes=HNDLR))
async def pin_message(client: Client, message):
    msg_id=message.message_id
    chat_id=message.chat.id
    if message.reply_to_message == None:
        await client.edit_message_text(chat_id , msg_id , "Shall I pin your head to wall ?")
    else:
        if message.chat.type == "private":
            reply_msg_id=message.reply_to_message.message_id
            await client.pin_chat_message(chat_id , reply_msg_id , both_sides=True)
            await message.edit_text("Done the Job master !")
        else:
            zuzu= await client.get_chat_member(chat_id , "me")
            can_pin=zuzu.can_pin_messages
            if not can_pin:
                await client.edit_message_text(chat_id , msg_id , "Not a admin bruh 🥱") 
            else:         
                reply_msg_id=message.reply_to_message.message_id
                await client.pin_chat_message(chat_id , reply_msg_id)
                await client.edit_message_text(chat_id , msg_id , "Done the Job master !")
