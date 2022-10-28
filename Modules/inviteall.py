
from config import (bot, HNDLR, SUDO_USERS, LOGS_CHANNEL)
from pyrogram import Client, filters

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["add"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["add"], prefixes=HNDLR))
async def copy_members(client, message):
      chat_id = message.text.split(None, 2)[1]
      m = await message.reply("~ Processing...")
      c = 0
      async for member in client.get_chat_members(chat_id):
            try:
              await client.iter_chat_members(message.chat.id, member.user.id)
              c += 1
            except Exception:
              pass
      try: 
        await m.delete()
        await message.delete()
        await message.reply(f" Done {c}")
      except:
        pass
print("🟢")
