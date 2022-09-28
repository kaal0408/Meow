
import time
import logging
import motor.motor_asyncio
from pyrogram import Client
from .config_var import Config

# Note StartUp Time - To Capture Uptime.

start_time = time.time()
meow_version = "V1.0"

# Enable Logging For Pyrogram
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [MeowUB] - %(levelname)s - %(message)s",
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("apscheduler").setLevel(logging.ERROR)


mongo_client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_DB)

# <-- Configuration Import -->
API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
SESSION = Config.STRING_SESSION
CMD_LIST = {}
sudo_id = Config.AFS

if not Config.STRING_SESSION:
    logging.error("No String Session Found!  Exiting!")
    quit(1)

if not Config.API_ID:
    logging.error("No Api-ID Found!  Exiting!")
    quit(1)

if not Config.API_HASH:
    logging.error("No ApiHash Found!  Exiting!")
    quit(1)

if not Config.LOG_GRP:
    logging.error("No Log Group ID Found!  Exiting!")
    quit(1)

# <-- User Client -->
Meow = Client(
    name = "[MEOW]",
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': "Main.Modules"}
)

# <-- Assistant Client -->

bot = Client(
    "LoverBoyXD",
    api_id= API_ID,
    api_hash= API_HASH,
    bot_token= BOT_TOKEN,
    plugins= {'root': "Main.Assistant"}
)




