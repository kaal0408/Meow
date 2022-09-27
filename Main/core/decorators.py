.

import os
import pytz
import inspect
import logging
from datetime import datetime
from traceback import format_exc
from pyrogram import ContinuePropagation, StopPropagation, filters
from pyrogram.errors.exceptions.bad_request_400 import (
    MessageIdInvalid,
    MessageNotModified,
    MessageEmpty,
    UserNotParticipant
)
from pyrogram.handlers import MessageHandler

from Main import (
    CMD_LIST,
    Config,
    Meow,
)
from Main.config_var import Config
from Main.helper_func.basic_helpers import is_admin_or_owner
from Main.core.helpers import edit_or_reply
from database.sudodb import sudo_list

from bot_utils_files.Localization.engine import Engine as engin_e

Engine = engin_e()


sudo_list_ = Meow.loop.create_task(sudo_list())

async def _sudo(f, client, message):
    if not message:
        return bool(False)
    if not message.from_user:
        return bool(False)
    if not message.from_user.id:
        return bool(False)
    if message.from_user.id in sudo_list_.result():
        return bool(True)
    return bool(False)

_sudo = filters.create(func=_sudo, name="_sudo")

def meow_on_cmd(
    cmd: list,
    group: int = 0,
    pm_only: bool = False,
    group_only: bool = False,
    channel_only: bool = False,
    only_if_admin: bool = False,
    ignore_errors: bool = False,
    propagate_to_next_handler: bool = True,
    disable_sudo: bool = False,
    file_name: str = None,
    is_official: bool = True,
    cmd_help: dict = {"help": "No One One Gonna Help You", "example": "{ch}what"},
):
    """- Main Decorator To Register Commands. -"""
    if disable_sudo:
        base_filters = (
        filters.me
        & filters.command(cmd, Config.COMMAND_HANDLER)
        & ~filters.via_bot
        & ~filters.forwarded
    )
    else:
        base_filters = (
            (filters.me | _sudo)
            & filters.command(cmd, Config.COMMAND_HANDLER)
            & ~filters.via_bot
            & ~filters.forwarded)
    cmd = list(cmd)
    add_help_menu(
        cmd=cmd[0],
        stack=inspect.stack(),
        is_official=is_official,
        cmd_help=cmd_help["help"],
        example=cmd_help["example"],
    )
    def decorator(func):
        async def wrapper(client, message):
            message.Engine = Engine
            message.client = client
            chat_type = message.chat.type
            if only_if_admin and not await is_admin_or_owner(
                message, (client.me).id
            ):
                await edit_or_reply(
                    message, "`This Command Only Works, If You Are Admin Of The Chat!`"
                )
                return
            if group_only and chat_type != "supergroup":
                await edit_or_reply(message, "`Are you sure this is a group?`")
                return
            if channel_only and chat_type != "channel":
                await edit_or_reply(message, "This Command Only Works In Channel!")
                return
            if pm_only and chat_type != "private":
                await edit_or_reply(message, "`This Cmd Only Works On PM!`")
                return
            if ignore_errors:
                await func(client, message)
            else:
                try:
                    await func(client, message)
                except StopPropagation:
                    raise StopPropagation
                except KeyboardInterrupt:
                    pass
                except MessageNotModified:
                    pass
                except MessageIdInvalid:
                    logging.warning(
                        "Please Don't Delete Commands While it's Processing.."
                    )
                except UserNotParticipant:
                    pass
                except ContinuePropagation:
                    raise ContinuePropagation
                except BaseException:
                    logging.error(
                        f"Exception - {func.__module__} - {func.__name__}"
                    )
                    TZ = pytz.timezone(Config.TZ)
                    datetime_tz = datetime.now(TZ)
                    text = "**!ERROR - REPORT!**\n\n"
                    text += f"\n**Trace Back : ** `{str(format_exc())}`"
                    text += f"\n**Plugin-Name :** `{func.__module__}`"
                    text += f"\n**Function Name :** `{func.__name__}` \n"
                    text += datetime_tz.strftime(
                        "**Date :** `%Y-%m-%d` \n**Time :** `%H:%M:%S`"
                    )
                    text += "\n\n__You can Forward This to @Murat_30, If You Think This is Serious A Error!__"
                    try:
                        await client.send_message(Config.LOG_GRP, text)
                    except BaseException:
                        logging.error(text)
        add_handler(base_filters, wrapper, cmd)
        return wrapper
    return decorator


def listen(filter_s):
    """Simple Decorator To Handel Custom Filters"""
    def decorator(func):
        async def wrapper(client, message):
            message.Engine = Engine
            try:
                await func(client, message)
            except StopPropagation:
                raise StopPropagation
            except ContinuePropagation:
                raise ContinuePropagation
            except UserNotParticipant:
                pass
            except MessageEmpty:
                pass
            except BaseException:
                logging.error(f"Exception - {func.__module__} - {func.__name__}")
                TZ = pytz.timezone(Config.TZ)
                datetime_tz = datetime.now(TZ)
                text = "**!ERROR WHILE HANDLING UPDATES!**\n\n"
                text += f"\n**Trace Back : ** `{str(format_exc())}`"
                text += f"\n**Plugin-Name :** `{func.__module__}`"
                text += f"\n**Function Name :** `{func.__name__}` \n"
                text += datetime_tz.strftime(
                    "**Date :** `%Y-%m-%d` \n**Time :** `%H:%M:%S`"
                )
                text += "\n\n__You can Forward This to @Murat_30, If You Think This is A Error!__"
                try:
                    await client.send_message(Config.LOG_GRP, text)
                except BaseException:
                    logging.error(text)
            message.continue_propagation()
        Meow.add_handler(MessageHandler(wrapper, filters=filter_s), group=0)
        return wrapper

    return decorator




def add_handler(filter_s, func_, cmd):
    d_c_l = Config.DISABLED_SUDO_CMD_S
    if d_c_l:
        d_c_l = d_c_l.split(" ")
        d_c_l = list(d_c_l)
        if "dev" in d_c_l:
            d_c_l.extend(['eval', 'bash', 'install']) 
        if any(item in list(d_c_l) for item in list(cmd)): 
            filter_s = (filters.me & filters.command(cmd, Config.COMMAND_HANDLER) & ~filters.via_bot & ~filters.forwarded)
    Meow.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    
