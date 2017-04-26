import pymongo

class Database(object):
    #universal resource identifier
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    #not going to be using self! -- use @staticmethod
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)


