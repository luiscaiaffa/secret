__all__ = ["Core"]
from .standalone import MongoConnection


class Core:

    @staticmethod
    def SetConfig(app, **confs):
        app.config.MONGO_URIS = confs
        return app

    def __init__(self, app=None,):
        self.mongodbs = {}
        if app:
            self.init_app(app)
        else:
            pass

    def init_app(self, app):
        if app.config.MONGO_URIS and isinstance(app.config.MONGO_URIS, dict):
            self.MONGO_URIS = app.config.MONGO_URIS
            self.app = app

        else:
            raise ValueError(
                "nonstandard sanic config MONGO_URIS,MONGO_URIS must be a Dict[dbname,dburl]")

        @app.listener("before_server_start")
        async def init_mongo_connection(app, loop):
            for dbname, dburl in app.config.MONGO_URIS.items():
                if isinstance(dburl,str):
                    db = MongoConnection(dburl,ioloop=loop).db
                else:
                    db = MongoConnection(ioloop=loop,**dburl).db
                self.mongodbs[dbname] = db

        @app.listener("before_server_stop")
        async def sub_close(app, loop):
            for dbname,db in self.mongodbs.items():
                db.client.close

        if "extensions" not in app.__dir__():
            app.extensions = {}
        app.extensions['SanicMongo'] = self

        app.mongo = self.mongodbs
        return self
