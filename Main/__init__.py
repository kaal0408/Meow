
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



if Config.STRING_SESSION:
    Meow = Client(
        Config.STRING_SESSION,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=dict(root="Main.Modules"))
        sleep_threshold=180,
    )


if Config.BOT_TOKEN:
    bot = Client(
        "MyAssistant",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="Main.Assistant"))
        sleep_threshold=180,
    )
else:
    bot = None
