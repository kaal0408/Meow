from database import dtbs

afk = dtbs["AFK"]

def go_afk(time, reason=""):
    
    midhun = afk.find_one({"_id": "AFK"})
    if midhun:
        afk.update_one({"_id": "AFK"}, {"$set": {"time": time, "reason": reason}})
    else:
        afk.insert_one({"_id": "AFK", "time": time, "reason": reason})

def no_afk():
    midhun = afk.find_one({"_id": "AFK"})
    if midhun:
        afk.delete_one({"_id": "AFK"})
    
def check_afk():
    midhun = afk.find_one({"_id": "AFK"})
    if midhun:
        return midhun
    else:
        return False
