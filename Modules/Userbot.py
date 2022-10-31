
import os
import sys
import asyncio
import datetime
import time
from config import bot
from config import (HNDLR, SUDO_USERS, ALIVE_PIC, ALIVE_MSG, PING_MSG, __version__, start_time)
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__ as pyro_vr             
                

pongg = PING_MSG if PING_MSG else "Meow is on fire"
KAAL_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/3c2932815330a143fa1a8.png"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "Meow is online now."


manjeet = f"⁂ {Alivemsg} ⁂\n\n"
manjeet += f"━───────╯•╰───────━\n"
manjeet += f"➠ **Python version** : `3.10.4`\n"
manjeet += f"➠ **Pyrogram version** : `{pyro_vr}`\n"
manjeet += f"➠ **version**  : `{__version__}`\n"
manjeet += f"➠ **Kali Linux**  : `Yes`\n"
manjeet += f"➠ **Database**  : `Mongo atlas`\n"
manjeet += f"➠ **Database Status **  : `Functional`\n"
manjeet += f"➠ **current Branch**  : `Master`\n"
manjeet += f"➠ **VC Modulesc**  : `Allow`\n"
manjeet += f"➠ **Channel** : [support channel](https://t.me/visionstudio_op)\n"
manjeet += f"➠ **Group** : [Owner](https://t.me/Murat_30)\n"
manjeet += f"━───────╮•╭───────━\n\n"
manjeet += f"➠ **Channel** : [Commands](https://t.me/VisionStudio_op/32)\n"
manjeet += f"➠ **Source Code:** [•Repo•](https://github.com/kaal0408/Meow)"


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")




@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["alive"], prefixes=HNDLR))
async def alive(xspam: Client, e: Message):
       if ".jpg" in KAAL_PIC or ".png" in KAAL_PIC:
              await xspam.send_photo(e.chat.id, KAAL_PIC, caption=manjeet)
       if ".mp4" in KAAL_PIC or ".MP4," in KAAL_PIC:
              await xspam.send_video(e.chat.id, KAAL_PIC, caption=manjeet)






@Client.on_message(filters.user(SUDO_USERS) & filters.command(["restart", "reboot"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["restart", "reboot"], prefixes=HNDLR))
async def restart_bot(_, message: Message):
    msg = await message.reply("`restarting bot...`")
    args = [sys.executable, "main.py"]
    await msg.edit("✅ bot restarted\n\n• now you can use this bot again.")
    execle(sys.executable, *args, environ)
    return
            
