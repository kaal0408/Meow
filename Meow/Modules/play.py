from pytgcalls import idle as pyidle
import os
import json
import shutil
from config import config
from core.song import Song
from pyrogram.types import Message
from pytgcalls.types import Update
from pyrogram import Client, filters
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded
from core.decorators import language, register, only_admins, handle_error
from core import (
    app, ydl, search, is_sudo, sweetie, is_admin, get_group, get_queue,
    pytgcalls, set_group, set_title, all_groups, clear_queue, skip_stream,
    check_yt_url, extract_args, start_stream, shuffle_queue, delete_messages,
    get_spotify_playlist, get_youtube_playlist)



client = app


@client.on_message(filters.user(SUDO_USERS) & filters.command(["play"], prefixes=HNDLR))
@client.on_message(filters.me & filters.command(["play"], prefixes=HNDLR))
@register
@language
@handle_error
async def play_stream(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if group["admins_only"]:
        check = await is_admin(message)
        if not check:
            k = await message.reply_text(lang["notAllowed"])
            return await delete_messages([message, k])
    song = await search(message)
    if song is None:
        k = await message.reply_text(lang["notFound"])
        return await delete_messages([message, k])
    ok, status = await song.parse()
    if not ok:
        raise Exception(status)
    if not group["is_playing"]:
        set_group(chat_id, is_playing=True, now_playing=song)
        await start_stream(song, lang)
        await delete_messages([message])
    else:
        queue = get_queue(chat_id)
        await queue.put(song)
        k = await message.reply_text(
            lang["addedToQueue"] % (song.title, song.source, len(queue)),
            disable_web_page_preview=True,
        )
        await delete_messages([message, k])

@client.on_message(filters.user(SUDO_USERS) & filters.command(["radio"], prefixes=HNDLR))
@client.on_message(filters.me & filters.command(["radio"], prefixes=HNDLR))
@register
@language
@handle_error
async def live_stream(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if group["admins_only"]:
        check = await is_admin(message)
        if not check:
            k = await message.reply_text(lang["notAllowed"])
            return await delete_messages([message, k])
    args = extract_args(message.text)
    if args is None:
        k = await message.reply_text(lang["notFound"])
        return await delete_messages([message, k])
    if " " in args and args.count(" ") == 1 and args[-5:] == "parse":
        song = Song({"source": args.split(" ")[0], "parsed": False}, message)
    else:
        is_yt_url, url = check_yt_url(args)
        if is_yt_url:
            meta = ydl.extract_info(url, download=False)
            formats = meta.get("formats", [meta])
            for f in formats:
                ytstreamlink = f["url"]
            link = ytstreamlink
            song = Song(
                {"title": "YouTube Stream", "source": link, "remote": link}, message
            )
        else:
            song = Song(
                {"title": "Live Stream", "source": args, "remote": args}, message
            )
    ok, status = await song.parse()
    if not ok:
        raise Exception(status)
    if not group["is_playing"]:
        set_group(chat_id, is_playing=True, now_playing=song)
        await start_stream(song, lang)
        await delete_messages([message])
    else:
        queue = get_queue(chat_id)
        await queue.put(song)
        k = await message.reply_text(
            lang["addedToQueue"] % (song.title, song.source, len(queue)),
            disable_web_page_preview=True,
        )
        await delete_messages([message, k])


@client.on_message(filters.user(SUDO_USERS) & filters.command(["skip"], prefixes=HNDLR))
@client.on_message(filters.me & filters.command(["skip"], prefixes=HNDLR))
@register
@language
@only_admins
@handle_error
async def skip_track(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if group["loop"]:
        await skip_stream(group["now_playing"], lang)
    else:
        queue = get_queue(chat_id)
        if len(queue) > 0:
            next_song = await queue.get()
            if not next_song.parsed:
                ok, status = await next_song.parse()
                if not ok:
                    raise Exception(status)
            set_group(chat_id, now_playing=next_song)
            await skip_stream(next_song, lang)
            await delete_messages([message])
        else:
            set_group(chat_id, is_playing=False, now_playing=None)
            await set_title(message, "")
            try:
                await pytgcalls.leave_group_call(chat_id)
                k = await message.reply_text(lang["queueEmpty"])
            except (NoActiveGroupCall, GroupCallNotFound):
                k = await message.reply_text(lang["notActive"])
            await delete_messages([message, k])

@client.on_message(filters.user(SUDO_USERS) & filters.command(["mute"], prefixes=HNDLR))
@client.on_message(filters.me & filters.command(["mute"], prefixes=HNDLR))
@register
@language
@only_admins
@handle_error
async def mute_vc(_, message: Message, lang):
    chat_id = message.chat.id
    try:
        await pytgcalls.mute_stream(chat_id)
        k = await message.reply_text(lang["muted"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])

@client.on_message(filters.user(SUDO_USERS) & filters.command(["unmute"], prefixes=HNDLR))
@client.on_message(filters.me & filters.command(["unmute"], prefixes=HNDLR))
@register
@language
@only_admins
@handle_error
async def unmute_vc(_, message: Message, lang):
    chat_id = message.chat.id
    try:
        await pytgcalls.unmute_stream(chat_id)
        k = await message.reply_text(lang["unmuted"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])

@client.on_message(filters.user(SUDO_USERS) & filters.command(["pause"], prefixes=HNDLR))
@client.on_message(filters.me & filters.command(["pause"], prefixes=HNDLR))
@register
@language
@only_admins
@handle_error
async def pause_vc(_, message: Message, lang):
    chat_id = message.chat.id
    try:
        await pytgcalls.pause_stream(chat_id)
        k = await message.reply_text(lang["paused"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])

@client.on_message(filters.user(SUDO_USERS) & filters.command(["resume"], prefixes=HNDLR))
@client.on_message(filters.me & filters.command(["resume"], prefixes=HNDLR))
@register
@language
@only_admins
@handle_error
async def resume_vc(_, message: Message, lang):
    chat_id = message.chat.id
    try:
        await pytgcalls.resume_stream(chat_id)
        k = await message.reply_text(lang["resumed"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])

@client.on_message(filters.user(SUDO_USERS) & filters.command(["vcleave"], prefixes=HNDLR))
@client.on_message(filters.me & filters.command(["vcleave"], prefixes=HNDLR))
@register
@language
@only_admins
@handle_error
async def leave_vc(_, message: Message, lang):
    chat_id = message.chat.id
    set_group(chat_id, is_playing=False, now_playing=None)
    await set_title(message, "")
    clear_queue(chat_id)
    try:
        await pytgcalls.leave_group_call(chat_id)
        k = await message.reply_text(lang["leaveVC"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])
