from urllib.parse import quote_plus

from bson.objectid import ObjectId
from configuration import conf
from motor import motor_asyncio


class MongoDB:
    def __init__(self):
        if conf.bot.debug:
            self.client = motor_asyncio.AsyncIOMotorClient(host="localhost", port=27017)
        else:
            self.client = motor_asyncio.AsyncIOMotorClient(
                host=conf.db.host,
                port=conf.db.port,
                username=quote_plus(conf.db.username),
                password=quote_plus(conf.db.password),
            )
        self.db = self.client[conf.db.database]

    async def user_update(self, user_id, data=None):
        user_info = await self.db.users.find_one({"user_id": user_id})

        if user_info is None:
            await self.db.users.insert_one({"user_id": user_id})
            return await self.user_update(user_id, data)

        if data:
            await self.db.users.update_one(
                {"user_id": user_id}, {"$set": data}, upsert=True
            )
            return await self.user_update(user_id)

        return user_info

    async def users_list(self):
        return await self.db.users.find().to_list(length=None)


db = MongoDB()
