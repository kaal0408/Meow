import asyncio
import math
import os
import glob
import importlib
import ntpath
from pyrogram.types import Message
from Meow import SUDO_USERS as SUDO
from Meow import app
from pyrogram import enums


async def edit_or_reply(msg: Message, text, parse_mode=enums.ParseMode.MARKDOWN):
    if not msg:
        return await msg.edit(text, parse_mode=parse_mode)
    if not msg.from_user:
        return await msg.edit(text, parse_mode=parse_mode)
    if msg.from_user.id in SUDO:
        if msg.reply_to_message:
            kk = msg.reply_to_message.message_id
            return await msg.reply_text(
                text, reply_to_message_id=kk, parse_mode=parse_mode
            )
        return await msg.reply_text(text, parse_mode=parse_mode)
    return await msg.edit(text, parse_mode=parse_mode)

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.type == "text_mention":
                    user_s = int(required_entity.user.id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_

async def is_admin_or_owner(message, user_id) -> bool:
    """Check If A User Is Creator Or Admin Of The Current Group"""
    if message.chat.type == enmus.ChatType.PRIVATE:
        # You Are Boss Of Pvt Chats.
        return True
    user_s = await message.chat.get_member(int(user_id))
    if user_s.status in ("creator", "administrator"):
        return True
    return False

async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: app,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode=enums.ParseMode.MARKDOWN,
):
    """Send As File If Len Of Text Exceeds Tg Limit Else Edit Message"""
    if not text:
        await message.edit("`Wait, What?`")
        return
    if len(text) > 1024:
        await message.edit("`OutPut is Too Large, Sending As File!`")
        file_names = f"{file_name}.txt"
        open(file_names, "w").write(text)
        await client.send_document(message.chat.id, file_names, caption=caption)
        await message.delete()
        if os.path.exists(file_names):
            os.remove(file_names)
        return
    else:
        return await message.edit(text, parse_mode=parse_mode)


class Logme:
    def init(self, message):
        self.chat_id = LOGS_CHANNEL
        self.message = message
    async def fwd_msg_to_log_chat(self):
        try:
            return await self.message.forward(self.chat_id)
        except BaseException as e: 
            logging.error(str(e))
            return None
