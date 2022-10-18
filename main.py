import asyncio
from pytgcalls import idle
from config import call_py, bot


async def main():
    print("STARTING Pyrogram CLIENT")
    await bot.start()
    print("STARTING PYTGCALLS CLIENT")
    await call_py.start()
    print(
        """
    ------------------------
   | Meow userbot +  Music Actived! |
    ------------------------
"""
    )
    await idle()
    await pidle()
    print("STOPPING USERBOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
