from pyrogram import Client
from pyrogram.types import Message
from Meow.VC import *
from Meow.VC.decorators import errors, sudo_users_only
from Meow.VC.handlers import skip_current_song, skip_item
from Meow.VC.queues import QUEUE, clear_queue
from Meow import HNDLR, LOGS_CHANNEL, SUDO_USERS, call_py


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["skip"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["skip"], prefixes=HNDLR))
@errors
@sudo_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**❌ 𝑻𝒉𝒆𝒓𝒆'𝒔 𝒏𝒐𝒕𝒉𝒊𝒏𝒈 𝒊𝒏 𝒕𝒉𝒆 𝒒𝒖𝒆𝒖𝒆 𝒕𝒐 𝒔𝒌𝒊𝒑**")
        elif op == 1:
            await m.reply("**𝑬𝒎𝒑𝒕𝒚 𝒒𝒖𝒆𝒖𝒆 𝒍𝒆𝒂𝒗𝒊𝒏𝒈 𝒗𝒐𝒊𝒄𝒆 𝒄𝒉𝒂𝒕**")
        else:
            await m.reply(
                f"**⏩ 𝑺𝒌𝒊𝒑𝒑𝒆𝒅 𝒑𝒍𝒂𝒚𝒃𝒂𝒄𝒌** \n**🎶 𝑵𝒐𝒘 𝒑𝒍𝒂𝒚𝒊𝒏𝒈** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ 𝑹𝒆𝒎𝒐𝒗𝒆𝒅 𝒕𝒉𝒆 𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈 𝒔𝒐𝒏𝒈𝒔 𝒇𝒓𝒐𝒎 𝒕𝒉𝒆 𝑸𝒖𝒆𝒖𝒆: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["end"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["end"], prefixes=HNDLR))
@errors
@sudo_users_only
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✅ 𝑬𝒏𝒅𝒆𝒅 𝒑𝒍𝒂𝒚𝒃𝒂𝒄𝒌**")
        except Exception as e:
            await m.reply(f"**𝑬𝒓𝒓𝒐𝒓....** \n`{e}`")
    else:
        await m.reply("**❌ 𝑵𝒐𝒕𝒉𝒊𝒏𝒈 𝒊𝒔 𝒑𝒍𝒂𝒚𝒊𝒏𝒈**")



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["pause"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["pause"], prefixes=HNDLR))
@errors
@sudo_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ 𝑷𝒍𝒂𝒚𝒃𝒂𝒄𝒌 𝒑𝒂𝒖𝒔𝒆𝒅**\n\n𝑻𝒐 𝒓𝒆𝒔𝒖𝒎𝒆 𝒑𝒍𝒂𝒚𝒃𝒂𝒄𝒌, 𝒖𝒔𝒆 𝒕𝒉𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 » `!resume`"
            )
        except Exception as e:
            await m.reply(f"**𝑬𝒓𝒓𝒐𝒓.....** \n`{e}`")
    else:
        await m.reply("**❌ 𝑵𝒐𝒕𝒉𝒊𝒏𝒈 𝒊𝒔 𝒑𝒍𝒂𝒚𝒊𝒏𝒈**")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["resume"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["resume"], prefixes=HNDLR))
@errors
@sudo_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶️ 𝑷𝒍𝒂𝒚𝒃𝒂𝒄𝒌 𝒓𝒆𝒔𝒖𝒎𝒆𝒅**\n\n𝑻𝒐 𝒑𝒂𝒖𝒔𝒆 𝒑𝒍𝒂𝒚𝒃𝒂𝒄𝒌, 𝒖𝒔𝒆 𝒕𝒉𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 » `!pause`"
            )
        except Exception as e:
            await m.reply(f"**𝑬𝒓𝒓𝒐𝒓....** \n`{e}`")
    else:
        await m.reply("**❌ 𝑵𝒐𝒕𝒉𝒊𝒏𝒈 𝒊𝒔 𝒑𝒍𝒂𝒚𝒊𝒏𝒈**")
