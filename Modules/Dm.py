

import os
import sys
import asyncio
from random import choice
from config import (bot, HNDLR, SUDO_USERS, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from Modules.helpers.data import *

Usage = f"**❌ Wrong Usage ❌** \n Type: `{HNDLR}help dm`"


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["dmraid"], prefixes=HNDLR))
async def dmraid(xspam: Client, e: Message):
      """ Module: Dm Raid """
      Kaal = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Kaal) == 2:
          ok = await xspam.get_users(Kaal[1])
          id = ok.id
          if int(id) in KAALX:
                text = f"I can't raid on @kaalxsupport Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              counts = int(KAAL[0])
              await e.reply_text("⚜️ Dm Raid Started Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in KAALX:
                text = f"I can't raid on @kaalxsupport Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              counts = int(KAAL[0])
              await e.reply_text("⚜️ Dm Raid Started Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started DM Raid By User: {e.from_user.id} \n\n On User: {id} \n Counts: {counts}")
         except Exception as a:
             print(a)
             pass
 
     
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["dm"], prefixes=HNDLR))
async def dm(xspam: Client, e: Message):
      Kaal = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Kaal) == 2:
          usr = str(Kaal[0])
          ok = await xspam.get_users(usr)
          id = ok.id
          if int(id) in KAALX:
                text = f"I can't raid on @kaalxsupport Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              msg = str(KAAL[1])
              await e.reply_text("🔸 Message Delivered 🔸")
              await xspam.send_message(id, msg)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in KAALX:
                text = f"I can't raid on @KAALXSUPPORT Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              msg = str(KAAL[0])
              await e.reply_text("🔸 Message Delivered 🔸️")
              await xspam.send_message(id, msg)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"Direct Message By User: {e.from_user.id} \n\n On User: {id}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(filters.me & filters.command(["dmspam"], prefixes=HNDLR))
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
async def dmspam(xspam: Client, e: Message):
      Kaal = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      Kaalop = Kaal[1:]
      if len(Kaalop) == 2:
          msg = str(Kaalop[1])
          ok = await xspam.get_users(Rizoel[0])
          id = ok.id
          if int(id) in KAALX:
                text = f"I can't raid on @kaalxsupport Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              counts = int(Kaalop[0])
              await e.reply_text("☢️ Dm Spam Started ☢️")
              for _ in range(counts):
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in KAALX:
                text = f"I can't raid on @kaalxsupport Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              counts = int(Kaal[0])
              msg = str(Kaalop[0])
              await e.reply_text("☢️ Dm Spam Started ☢️")
              for _ in range(counts):
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started DM Spam By User: {e.from_user.id} \n\n On User: {id} \n Counts: {counts} \n Message: {msg}")
         except Exception as a:
             print(a)
             pass
