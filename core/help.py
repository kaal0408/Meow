import asyncio
from helpers.filters import command
from pyrogram import Client, filters
from config import BOT_NAME, START_IMG, SUPPORT_GROUP
from pyrogram.types import (
    Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup)


@Client.on_message(command("help") & filters.private & ~filters.group & ~filters.edited)
async def help_cmd(client: Client, message: Message):
    await message.reply_sticker(
        "CAACAgUAAx0CZIiVngABAoCAYqWU-JzBZtfz14vr_DfDkJyy7X8AAjYGAAIsk1lUo7RMhQfOm28eBA"
    )
    await message.reply_photo(
        f"{START_IMG}",
        caption=f"""
❄ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ {BOT_NAME} :**

๏ /play : sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.
๏ /pause : ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.
๏ /resume : ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.
๏ /skip : sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.
๏ /end : ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.
๏ /ping : sʜᴏᴡ ᴛʜᴇ ᴩɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /join : ʀᴇǫᴜᴇsᴛ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ᴊᴏɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.
๏ /id : sᴇɴᴅs ʏᴏᴜ ᴛʜᴇ ɪᴅ ᴏғ ᴛʜᴇ ᴜsᴇʀ ᴏʀ ʀᴇᴩʟɪᴇᴅ ғɪʟᴇ.
๏ /song : ᴅᴏᴡɴʟᴏᴀᴅs ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.
๏ /search : sᴇᴀʀᴄᴇs ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ ᴏɴ ʏᴏᴜᴛᴜʙᴇ ᴀɴᴅ sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʀᴇsᴜʟᴛ.

✨ **sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs :**

๏ /broadcast : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /eval or /sh : ʀᴜɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴏᴅᴇ ᴏɴ ᴛʜᴇ ʙᴏᴛ's ᴛᴇʀᴍɪɴᴀʟ.
๏ /rmw : ᴄʟᴇᴀʀs ᴀʟʟ ᴛʜᴇ ᴄᴀᴄʜᴇ ᴩʜᴏᴛᴏs ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /rmp : ᴄʟᴇᴀʀs ᴛʜᴇ ʀᴀᴡ ғɪʟᴇs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /rmd : ᴄʟᴇᴀʀs ᴛʜᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ғɪʟᴇs ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 sᴜᴩᴩᴏʀᴛ 💫", url=f"https://t.me/DollxSpam_BOT"
                    ),
                    InlineKeyboardButton(
                        "❄ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​ ❄",
                        url="https://t.me/DollxSpam_BOT",
                    ),
                ],
                [InlineKeyboardButton("✨ ᴄʟᴏsᴇ ✨", callback_data="close_play")],
            ]
        ),
    )
