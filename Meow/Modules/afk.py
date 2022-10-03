# All © Copyrights are reversed by Team of Astro2.0
# This file is part of Astro2.0
# https://github.com/AstroUb/Astro2.0


from pyrogram import filters
from pyrogram import enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
import asyncio
from startup.config import PVT_GRP
from . import *
from misc import *

from startup.dB.afkdb import (
    no_afk,
    go_afk,
    check_afk
)



@astro.on_message(filters.command("afk", HNDLR) & filters.me)
async def set_afk(_, message: Message):
    name = message.from_user.mention
    pablo = await edit_or_reply(message, "__Processing...__")
    msge = None
    msge = get_text(message)
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    log = Logme(message)
    if msge:
        msg = f"**{name}** \n__Going Afk Because Of😴💤__ `{msge}`"
        await log.log_msg(astro, f"#AfkLogger\n\nMaster your AFK is Activated✅\nR E A S O N: `{msge}`",)
        go_afk(afk_start, msge)
    else:
        msg = f"**AFK**Started✅\n\nR E A S O N: **I am very Busy Right Now🥵🥵\nI can't talk to your now!!😅\n\nPlease Wait until i will come back😁**."
        await log.log_msg(astro, f"#AfkLogger Afk Is Active")
        go_afk(afk_start) 
    await pablo.edit(msg)
        
@dynamic(filters.mentioned & ~filters.me & ~filters.bot & filters.incoming)
async def afk_er(astro, message: Message):
    lol = check_afk()
    if not lol:
        message.continue_propagation()
    reason = lol["reason"]
    if reason == "":
        reason = None
    back_alivee = datetime.now()
    chat = message.chat
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    afk_since = "**a while ago**"
    message_to_reply = (f"I Am **AFK** Right Now.💤😴\n\n**Reason🤔⁉️** : `{reason}`\n\n**Last Seen⌛⏲️:** `{total_afk_time}`" if reason else f"I Am **AFK** Right Now.💤😴\n\n**REASON**🤔⁉️: `I am very Busy Right Now🥵🥵\nI can't talk to your now!!😅\n\nPlease Wait until i will come back😁`\n\n**Last Seen⏲️⌛:** `{total_afk_time}`")
    LL = await message.reply(message_to_reply)
    if chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
      try: 
        await assistant.send_message(PVT_GRP, f"#TAGGED\n\nHey!\nMy Honorable Master Someone has tagged you in group while you were in AFK!\n\n~CHAT👥: - {chat.title}\n~Message📜: - {message.text}\n", reply_markup=InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            text="📨Check Message", url=f"https://t.me/c/{str(chat.id)[4:]}/{message.id}")
    ]
    ]),
   )
      except ValueError:
        await astro.send_message(PVT_GRP, "Master\nYou have not Added Your assistant bot here😅\nWithout Assistant you can't get Tagged Notification\n\nPlease add Assistant Here!")
    message.continue_propagation()
        
@dynamic(filters.outgoing & filters.me)
async def no_afke(astro, message: Message):
    name = message.from_user.mention
    lol = check_afk()
    if not lol:
        message.continue_propagation()
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    kk = await message.reply(f"""{name} is Back Alive__\n**No Longer afk.**\n `I Was afk for:``{total_afk_time}`""",)
    await asyncio.sleep(9)
    await kk.delete()
    no_afk()
    log = Logme(message)
    await log.log_msg(astro, f"#AfkLogger {name} is Back Alive ! No Longer Afk\n AFK for : {total_afk_time} ")
    message.continue_propagation()
