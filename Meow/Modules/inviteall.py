
from Meow import (app, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters

@app.on_message(filters.user(SUDO_USERS) & filters.command(["add"], prefixes=HNDLR))
@app.on_message(filters.me & filters.command(["add"], prefixes=HNDLR))
async def copy_members(client, message):
      chat_id = message.text.split(None, 2)[1]
      m = await message.reply("~ Processing...")
      c = 0
      async for member in app.get_chat_members(chat_id):
            try:
              await app.add_chat_members(message.chat.id, member.user.id)
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
