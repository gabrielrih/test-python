import pymongo

from resources.atlas.mongo_cfg import MongoCfg
from resources.atlas.exception.mongo_exception import MongoException

class Mongo():
    def __init__(self):
        self.credential = MongoCfg()

    def open_connection(self):
        self.client = pymongo.MongoClient(self.credential.connection_string, serverSelectionTimeoutMS=self.credential.time_out_in_ms)
        try:
            self.client.server_info()
        except MongoException as exc:
            raise exc

    def insert_a_document(self, database_name: str, collection_name: str, json: str):
        if not self.client:
            raise 'Exception: You must open a connection first!'
        try:
            database = self.client[database_name]
            collection = database[collection_name]
            collection.insert_one(json)
        except MongoException as exc:
            raise exc
        