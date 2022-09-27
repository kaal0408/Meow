

from database import db_x

broadcast_db = db_x["BROADCAST_DB"]


async def add_broadcast_chat(chat_id):
    await broadcast_db.insert_one({"chat_id": chat_id})


async def rmbroadcast_chat(chat_id):
    await broadcast_db.delete_one({"chat_id": chat_id})


async def get_all_broadcast_chats():
    return [la async for la in broadcast_db.find({})]


async def is_broadcast_chat_in_db(chat_id):
    k = await broadcast_db.find_one({"chat_id": chat_id})
    return bool(k)
