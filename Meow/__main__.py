# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang 


from pytgcalls import idle
import asyncio
from pyrogram import idle
from . import (app, hl, arq, call_py)


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | ƲՏЄƦƁƠƬ ƛƇƬƖƔЄƊ! |
    ------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


