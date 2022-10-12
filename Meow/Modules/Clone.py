import os
from pyrogram import *
from handlers.help import *
from pyrogram.types import *
from helpers.basic import edit_or_reply, get_text, get_user


OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "Lҽɠҽɳԃαɾყ Oϝ Meow UʂҽɾႦσƚ")


from Meow import (app, app2, app3, app4, app5, HNDLR, SUDO_USERS, LOGS_CHANNEL )
from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["clone"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["clone"], prefixes=HNDLR))
async def clone(client: Client, message: Message):
  text = get_text(message)
  op = await edit_or_reply(message, "`Cloning`")
  userk = get_user(message, text)[0]
  user_ = await client.get_users(userk)
  if not user_:
    await op.edit("`Whom i should clone:(`")
    return
    
  get_bio = await client.get_chat(user_.id)
  f_name = user_.first_name
  c_bio = get_bio.bio
  pic = user_.photo.big_file_id
  poto = await client.download_media(pic)

  await client.set_profile_photo(photo=poto)
  await client.update_profile(
       first_name=f_name,
       bio=c_bio,
  )
  await message.edit(f"**From now I'm** __{f_name}__")
    
#from Meow import (app, app2, app3, app4, app5, HNDLR, SUDO_USERS, LOGS_CHANNEL )
#from pyrogram import Client, filters


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["revert"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["revert"], prefixes=HNDLR))
async def revert(client: Client, message: Message):
 await message.edit("`Reverting`")
 r_bio = BIO
	
	#Get ur Name back
 await client.update_profile(
	  first_name=OWNER,
	  bio=r_bio,
	)
	#Delte first photo to get ur identify
 photos = await client.get_profile_photos("me")
 await client.delete_profile_photos(photos[0].file_id)
 await message.edit("`I am back!`")



