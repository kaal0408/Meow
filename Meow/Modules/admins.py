from pyrogram import Client, filters
from pyrogram.types import Message

from Meow import HNDLR, LOGS_CHANNEL, SUDO_USERS, app, call_py
from Meow.Modules.helpers.decorators import authorized_users_only
from Meow.Modules.helpers.handlers import skip_current_song, skip_item
from Meow.Modules.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["skip"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["skip"], prefixes=HNDLR))
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**❌ There's nothing in the queue to skip!**")
        elif op == 1:
            await m.reply("Empty Queue, Leaving Voice Chat**")
        else:
            await m.reply(
                f"**⏭ SKIP PLAYED** \n**🎧 NOW PLAY** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ Removed the following songs from the Queue: -**"
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
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✅ END PLAYBACK**")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❌ NOTHING IS PLAYING!**")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["pause"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["pause"], prefixes=HNDLR))
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ PLAYBACK IS PAUSED.**\n\n• To resume playback, use the command » {HNDLR}resume"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("** ❌ NOTHING IS PLAYING!**")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["resume"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["resume"], prefixes=HNDLR))
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ RESUME PAUSED PLAYBACK**\n\n• To pause playback, use the command » {HNDLR}pause**"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❌ NOTHING IS CURRENTLY PAUSED!**")
