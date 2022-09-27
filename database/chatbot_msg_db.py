

from database import db_x

msg_db = db_x["CHATBOT_MSG_DB"]


async def add_msg_in_db(msg_id, sender_id, um_id):
    await msg_db.insert_one({"msg_id": msg_id, "sender_id": sender_id, "um_id": um_id})


async def get_user_id_frm_msg_id(msg_id):
    return await msg_db.find_one({"msg_id": msg_id})
