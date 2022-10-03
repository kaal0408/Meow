# Thanks to Friday!

from Meow import app
from Meow import LOGS_CHANNEL, TIMEZONE
from pyrogram import StopPropagation, filters, ContinuePropagation
from pyrogram.handlers import MessageHandler
from datetime import datetime
from traceback import format_exc
import logging
import pytz


def manjeet(filter_s):
    """Simple Decorator To Handel Custom Filters"""
    def decorator(func):
        async def wrapper(app, message):
            try:
                await func(app, message)
            except StopPropagation:
                raise StopPropagation
            except ContinuePropagation:
                raise ContinuePropagation
            except BaseException as e:
                logging.error(f"Exception - {func.__module__} - {func.__name__} : {e}")
                TZ = pytz.timezone(TIMEZONE)
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
                    await app.send_message(LOGS_CHANNEL, text)
                except Exception:
                    pass
        app.add_handler(MessageHandler(wrapper, filters=filter_s), group=0)
        return wrapper
    return decorator
