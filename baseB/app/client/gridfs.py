__all__ = ["Core"]
from .standalone import GridFSBucket


class Core:

    @staticmethod
    def SetConfig(app, **confs):
        app.config.GRIDFS_SETTINGS = confs
        return app

    def __init__(self, app):
        self.GridFSs = {}
        if app:
            self.init_app(app)
        else:
            pass

    def init_app(self, app):

        if app.config.GRIDFS_SETTINGS and isinstance(app.config.GRIDFS_SETTINGS, dict):
            self.GRIDFS_SETTINGS = app.config.GRIDFS_SETTINGS
            self.app = app

        else:
            raise ValueError(
                "nonstandard sanic config GRIDFS_URIS,GRIDFS_URIS must be a Dict[Bucket_name,Tuple[dburl,collection]]")

        @app.listener("before_server_start")
        async def init_mongo_connection(app, loop):
            for bucket_name, (dburl,collection) in app.config.GRIDFS_SETTINGS.items():
                if isinstance(dburl,str):
                    bucket = GridFSBucket(dburl,ioloop=loop,collection = collection).bucket
                else:
                    bucket = GridFSBucket(ioloop=loop,collection = collection,**dburl).bucket
                self.GridFSs[bucket_name] = bucket

        @app.listener("before_server_stop")
        async def sub_close(app, loop):
            for bucket_name,bucket in self.GridFSs.items():
                bucket.client.close

        if "extensions" not in app.__dir__():
            app.extensions = {}
        app.extensions['SanicGridFS'] = self

        app.GridFS = self.GridFSs
        return self
