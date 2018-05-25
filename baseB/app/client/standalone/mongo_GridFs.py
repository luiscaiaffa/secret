from motor.motor_asyncio import AsyncIOMotorGridFSBucket
from .mongo_connection import MongoConnection


class GridFSBucket:
    def __init__(self, uri: str, ioloop=None,collection="fs", only_db=False):
        mongo = MongoConnection(uri=uri,ioloop=ioloop, only_db= only_db)
        fs = AsyncIOMotorGridFSBucket(mongo.db,collection=collection)
        setattr(fs, "client", mongo.client)
        self.bucket = fs
