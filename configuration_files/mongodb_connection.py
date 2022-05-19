from pymongo import MongoClient

class DatabaseInfo:
    def __init__(self):
        self.__database = 'New_Twitter'
        self.__collection = 'info'

    def get_database_connection(self):
        client = MongoClient('localhost:27017')
        return client.get_database(self.__database).get_collection(self.__collection)
