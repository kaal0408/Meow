import time

from pyrogram import filters, Client
from pyrogram.errors import UserAdminInvalid
from pyrogram.types import Message, ChatPermissions

from helpers.PyroHelpers import GetUserMentionable
from helpers.adminHelpers import CheckAdmin, CheckReplyAdmin, RestrictFailed
from Meow import (app, app2, app3, app4, app5, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["kick"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["kick"], prefixes=HNDLR))
async def kick_user(bot: Client, message: Message):
    if await CheckReplyAdmin(message) and await CheckAdmin(message):
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)

            await bot.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
            )

            await message.edit(f"Goodbye, {mention}.")
        except UserAdminInvalid:
            await RestrictFailed(message)



