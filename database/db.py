from config_reader import config
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection


class MongoDBase:
    uri = f"mongodb://{config.mongo_host.get_secret_value()}:{config.mongo_port.get_secret_value()}/"

    def __init__(self):
        self.db_client: AsyncIOMotorClient = AsyncIOMotorClient(self.uri)
        self.current_db: AsyncIOMotorDatabase = self.db_client[config.database_name.get_secret_value()]
        self.collection: AsyncIOMotorCollection = self.current_db[config.collection_name.get_secret_value()]

    async def aggregator(self, pipeline):
        result_list = await self.collection.aggregate(pipeline).to_list(length=None)
        return result_list

