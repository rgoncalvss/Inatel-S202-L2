import pymongo

class Database:
    def __init__(self, uri, database):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[database]

    def close(self):
        self.client.close()
