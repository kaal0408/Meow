from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from config import (bot, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["unpin"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["unpin"], prefixes=HNDLR))
async def unpin_message(client: Client, message: Message):
    msg_id=message.message_id
    chat_id=message.chat.id
    if message.reply_to_message == None:
        await client.edit_message_text(chat_id , msg_id , "Shall I unpin your head from wall ?")
    else:
        if message.chat.type == "private":
            reply_msg_id=message.reply_to_message.message_id
            await client.unpin_chat_message(chat_id , reply_msg_id )
            await client.edit_message_text(chat_id , msg_id , "Done the Job master !")
        else:
            zuzu=await RaiChUB.get_chat_member(chat_id , "me")
            can_pin=zuzu.can_pin_messages
            if can_pin == None:
                await client.edit_message_text(chat_id , msg_id , "Can't pin messages bruh 🥱") 
            else:         
                reply_msg_id=message.reply_to_message.message_id
                await client.unpin_chat_message(chat_id , reply_msg_id)
                await client.edit_message_text(chat_id , msg_id , "Done the Job master !")

