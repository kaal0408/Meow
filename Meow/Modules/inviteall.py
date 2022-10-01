from pyrogram import Client, filters



@app.on_message(filters.regex("!add") & filters.me) # example : !add @Y88F8
async def copy_members(client, message):
# by : @ZDDDU 
      chat_id = message.text.split(None, 2)[1]
     #by : @Murat_30 
      m = await message.reply("~ Processing...")
     #by : @Murat_30 
      c = 0
     #by : @Murat_30 
      async for member in app.get_chat_members(chat_id):
     #by : @Murat_30 
            try:
           #by : @Murat_30 
              await app.add_chat_members(message.chat.id, member.user.id)
             #by : @Murat_30 
              c += 1
             #by : @Murat_30 
            except Exception:
           #by : @Murat_30 
              pass
      try:
      
        await m.delete()
       #by : @Murat_30 
        await message.delete()
       #by : @Murat_30 
        await message.reply(f" Done {c}")
       #by : @Murat_30 
      except:
     #by : @Murat_30 
        pass
# by : @Murat_30
print("🟢")
