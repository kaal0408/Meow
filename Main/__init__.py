
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


Meow = Client(
    ":memory:",
    API_ID,
    API_HASH,
    session_name= STRING_SESSION,
    plugins=dict(root="Main.Modules")
)

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token= BOT_TOKEN,
    plugins=dict(root="Main.Assistant")
)




