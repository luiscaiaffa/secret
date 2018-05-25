from sanic import Sanic
from .client import Mongo

app = Sanic(__name__)
mongo_uri = "mongodb://secret_db_1:27017/basec"
Mongo.SetConfig(app, test=mongo_uri)
Mongo(app)

from app import views

