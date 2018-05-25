__all__ = ["Mongo", "GridFS"]

from .mongo import Core as MongoCore
from .gridfs import Core as GridFSCore


class Mongo(MongoCore):
    pass


class GridFS(GridFSCore):
    pass
