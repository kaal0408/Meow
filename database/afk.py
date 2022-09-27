

from database import db_x

afk = db_x["I_AFK"]


async def go_afk(time, reason=""):
    midhun = await afk.find_one({"_id": "AFK"})
    if midhun:
        await afk.update_one({"_id": "AFK"}, {"$set": {"time": time, "reason": reason}})
    else:
        await afk.insert_one({"_id": "AFK", "time": time, "reason": reason})


async def no_afk():
    midhun = await afk.find_one({"_id": "AFK"})
    if midhun:
        await afk.delete_one({"_id": "AFK"})


async def check_afk():
    midhun = await afk.find_one({"_id": "AFK"})
    if midhun:
        return midhun
    else:
        return None
