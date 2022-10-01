# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang Bitch -! 



import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters


if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.1"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
SESSION = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
SESSION16 = os.getenv("SESSION16", None)
SESSION17 = os.getenv("SESSION17", None)
SESSION18 = os.getenv("SESSION18", None)
SESSION19 = os.getenv("SESSION19", None)
SESSION20 = os.getenv("SESSION20", None)
SESSION21 = os.getenv("SESSION21", None)
SESSION22 = os.getenv("SESSION22", None)
SESSION23 = os.getenv("SESSION23", None)
SESSION24 = os.getenv("SESSION24", None)
SESSION25 = os.getenv("SESSION25", None)
SESSION26 = os.getenv("SESSION26", None)
SESSION27 = os.getenv("SESSION27", None)
SESSION28 = os.getenv("SESSION28", None)
SESSION29 = os.getenv("SESSION29", None)
SESSION30 = os.getenv("SESSION30", None)
SESSION31 = os.getenv("SESSION31", None)
SESSION32 = os.getenv("SESSION32", None)
SESSION33 = os.getenv("SESSION33", None)
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)

    
HNDLR = os.getenv("HNDLR", ".")
sudo = os.getenv("SUDO_USERS")

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
DEVS = [2068551800, 5174965229]
for x in DEVS:
    SUDO_USERS.append(x)




# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------

KAAL = Client(name="SESSION", api_id = API_ID, api_hash = API_HASH, session_string=SESSION, plugins=dict(root="Spam.module"))
print("Client 1 Found")


hl = HNDLR[0]
start_time = time.time()

#-------------------------CLIENTS-----------------------------

if SESSION2:
    KAAL2 = Client(name="SESSION2", api_id = API_ID, api_hash = API_HASH, session_string=SESSION2, plugins=dict(root="Spam.module"))
    print("Client 2 Found")
else:
    KAAL2 = None

if SESSION3:
    KAAL3 = Client(name="SESSION3", api_id = API_ID, api_hash = API_HASH, session_string=SESSION3, plugins=dict(root="Spam.module"))
    print("Client 3 Found")
else:
    KAAL3 = None

if SESSION4:
    KAAL4 = Client(name="SESSION4", api_id = API_ID, api_hash = API_HASH, session_string=SESSION4, plugins=dict(root="Spam.module"))
    print("Client 4 Found")
else:
    KAAL4 = None

if SESSION5:
    KAAL5 = Client(name="SESSION5", api_id = API_ID, api_hash = API_HASH, session_string=SESSION5, plugins=dict(root="Spam.module"))
    print("Client 5 Found")
else:
    KAAL5 = None

if SESSION6:
    KAAL6 = Client(name="SESSION6", api_id = API_ID, api_hash = API_HASH, session_string=SESSION6, plugins=dict(root="Spam.module"))
    print("Client 6 Found")
else:
    KAAL6 = None
        
if SESSION7:
    KAAL7 = Client(name="SESSION7", api_id = API_ID, api_hash = API_HASH, session_string=SESSION7, plugins=dict(root="Spam.module"))
    print("Client 7 Found")
else:
    KAAL7 = None

if SESSION8:
    KAAL8 = Client(name="SESSION8", api_id = API_ID, api_hash = API_HASH, session_string=SESSION9, plugins=dict(root="Spam.module"))
    print("Client 8 Found")
else:
    KAAL8 = None

if SESSION9:
    KAAL9 = Client(name="SESSION9", api_id = API_ID, api_hash = API_HASH, session_string=SESSION9, plugins=dict(root="Spam.module"))
    print("Client 9 Found")
else:
    KAAL9 = None

if SESSION10:
    KAAL10 = Client(name="SESSION10", api_id = API_ID, api_hash = API_HASH, session_string=SESSION10, plugins=dict(root="Spam.module"))
    print("Client 10 Found")
else:
    KAAL10 = None

if SESSION11:
    KAAL11 = Client(name="SESSION11", api_id = API_ID, api_hash = API_HASH, session_string=SESSION11, plugins=dict(root="Spam.module"))
    print("Client 11 Found")
else:
    KAAL11 = None

if SESSION12:
    KAAL12 = Client(name="SESSION12", api_id = API_ID, api_hash = API_HASH, session_string=SESSION12, plugins=dict(root="Spam.module"))
    print("Client 12 Found")
else:
    KAAL12 = None

if SESSION13:
    KAAL13 = Client(name="SESSION13", api_id = API_ID, api_hash = API_HASH, session_string=SESSION13, plugins=dict(root="Spam.module"))
    print("Client 13 Found")
else:
    KAAL13 = None

if SESSION14:
    KAAL14 = Client(name="SESSION14", api_id = API_ID, api_hash = API_HASH, session_string=SESSION14, plugins=dict(root="Spam.module"))
    print("Client 14 Found")
else:
    KAAL14 = None

if SESSION15:
    KAAL15 = Client(name="SESSION15", api_id = API_ID, api_hash = API_HASH, session_string=SESSION15, plugins=dict(root="Spam.module"))
    print("Client 15 Found")
else:
    KAAL15 = None

if SESSION16:
    KAAL16 = Client(name="SESSION16", api_id = API_ID, api_hash = API_HASH, session_string=SESSION16, plugins=dict(root="Spam.module"))
    print("Client 16 Found")
else:
    KAAL16 = None
    
if SESSION17:
    KAAL17 = Client(name="SESSION17", api_id = API_ID, api_hash = API_HASH, session_string=SESSION17, plugins=dict(root="Spam.module"))
    print("Client 17 Found")
else:
    KAAL17 = None   
    
if SESSION18:
    KAAL18 = Client(name="SESSION18", api_id = API_ID, api_hash = API_HASH, session_string=SESSION18, plugins=dict(root="Spam.module"))
    print("Client 18 Found")
else:
    KAAL18 = None     
    
if SESSION19:
    KAAL19 = Client(name="SESSION19", api_id = API_ID, api_hash = API_HASH, session_string=SESSION19, plugins=dict(root="Spam.module"))
    print("Client 19 Found")
else:
    KAAL19 = None    

if SESSION20:
    KAAL20 = Client(name="SESSION20", api_id = API_ID, api_hash = API_HASH, session_string=SESSION20, plugins=dict(root="Spam.module"))
    print("Client 20 Found")
else:
    KAAL20 = None

if SESSION21:
    KAAL21 = Client(name="SESSION21", api_id = API_ID, api_hash = API_HASH, session_string=SESSION21, plugins=dict(root="Spam.module"))
    print("Client 21 Found")
else:
    KAAL21 = None

if SESSION22:
    KAAL22 = Client(name="SESSION22", api_id = API_ID, api_hash = API_HASH, session_string=SESSION22, plugins=dict(root="Spam.module"))
    print("Client 22 Found")
else:
    KAAL22 = None

if SESSION23:
    KAAL23 = Client(name="SESSION23", api_id = API_ID, api_hash = API_HASH, session_string=SESSION23, plugins=dict(root="Spam.module"))
    print("Client 23 Found")
else:
    KAAL23 = None

if SESSION24:
    KAAL24 = Client(name="SESSION24", api_id = API_ID, api_hash = API_HASH, session_string=SESSION24, plugins=dict(root="Spam.module"))
    print("Client 24 Found")
else:
    KAAL24 = None

if SESSION25:
    KAAL25 = Client(name="SESSION25", api_id = API_ID, api_hash = API_HASH, session_string=SESSION25, plugins=dict(root="Spam.module"))
    print("Client 25 Found")
else:
    KAAL25 = None
        
if SESSION26:
    KAAL26 = Client(name="SESSION26", api_id = API_ID, api_hash = API_HASH, session_string=SESSION26, plugins=dict(root="Spam.module"))
    print("Client 26 Found")
else:
    KAAL26 = None

if SESSION27:
    KAAL27 = Client(name="SESSION27", api_id = API_ID, api_hash = API_HASH, session_string=SESSION27, plugins=dict(root="Spam.module"))
    print("Client 8 Found")
else:
    KAAL27 = None

if SESSION28:
    KAAL28 = Client(name="SESSION28", api_id = API_ID, api_hash = API_HASH, session_string=SESSION28, plugins=dict(root="Spam.module"))
    print("Client 28 Found")
else:
    KAAL28 = None

if SESSION29:
    KAAL29 = Client(name="SESSION29", api_id = API_ID, api_hash = API_HASH, session_string=SESSION29, plugins=dict(root="Spam.module"))
    print("Client 29 Found")
else:
    KAAL29 = None

if SESSION30:
    KAAL30 = Client(name="SESSION30", api_id = API_ID, api_hash = API_HASH, session_string=SESSION30, plugins=dict(root="Spam.module"))
    print("Client 30 Found")
else:
    KAAL30 = None

if SESSION31:
    KAAL31 = Client(name="SESSION31", api_id = API_ID, api_hash = API_HASH, session_string=SESSION31, plugins=dict(root="Spam.module"))
    print("Client 31 Found")
else:
    KAAL31 = None

if SESSION32:
    KAAL32 = Client(name="SESSION32", api_id = API_ID, api_hash = API_HASH, session_string=SESSION32, plugins=dict(root="Spam.module"))
    print("Client 32 Found")
else:
    KAAL32 = None

if SESSION33:
    KAAL33 = Client(name="SESSION33", api_id = API_ID, api_hash = API_HASH, session_string=SESSION33, plugins=dict(root="Spam.module"))
    print("Client 33 Found")
else:
    KAAL33 = None

