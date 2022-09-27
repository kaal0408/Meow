

from database import db_x

welcome = db_x["WELCOME"]


async def add_welcome(chat_id, message_id):
    stark = await welcome.find_one({"chat_id": chat_id})
    if stark:
        await welcome.update_one({"chat_id": chat_id}, {"$set": {"msg_id": message_id}})
    else:
        await welcome.insert_one({"chat_id": chat_id, "msg_id": message_id})


async def del_welcome(chat_id):
    await welcome.delete_one({"chat_id": chat_id})


async def welcome_info(chat_id):
    r = await welcome.find_one({"chat_id": chat_id})
    if r:
        return r
    else:
        return False
