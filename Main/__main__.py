
import logging
import os
import platform

import pyrogram
from pyrogram import __version__
from bot_utils_files.Localization.engine import Engine
from database.localdb import check_lang
from Main import (
    Meow,
    bot,
    meow_version,
    mongo_client,
)
from Main.core.startup_helpers import (
    run_cmd,
)

from .config_var import Config


async def mongo_check():
    """Check Mongo Client"""
    logging.info("[MONGO_CLIENT] - initializing Mongo Client..")
    try:
        await mongo_client.server_info()
    except BaseException as e:
        logging.error("Something Isn't Right With Mongo! Please Check Your URL")
        logging.error(str(e))
        quit(1)


        
Meow.selected_lang = check_lang()
LangEngine = Engine()
LangEngine.load_language() 
     
Meow.start()
Meow.join_chat("Kaalxsupport")
bot.start()
    
print("Your Meow  Successfully Deployed ✅")
  


