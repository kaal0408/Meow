

from database import db_x

autoposter = db_x["AutoPoster"]


async def add_new_autopost(to_channel, target_channel):
    await autoposter.insert_one(
        {"target_channel": int(target_channel), "to_channel": int(to_channel)}
    )


async def check_if_autopost_in_db(to_channel, target_channel):
    st = await autoposter.find_one(
        {"target_channel": int(target_channel), "to_channel": int(to_channel)}
    )
    return bool(st)


async def del_autopost(to_channel, target_channel):
    await autoposter.delete_one(
        {"target_channel": int(target_channel), "to_channel": int(to_channel)}
    )


async def get_autopost(target_channel):
    return [
        s
        async for s in autoposter.find({"target_channel": int(target_channel)})
    ]
