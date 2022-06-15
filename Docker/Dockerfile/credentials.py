from dotenv import load_dotenv
import os


class TwitterInfo:
    def __init__(self):
        load_dotenv()
        self.__consumer_key = os.getenv('CONSUMER_KEY')
        self.__consumer_secret = os.getenv('CONSUMER_SECRET')
        self.__access_token = os.getenv('ACCESS_TOKEN')
        self.__access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    def get_consumer_key(self):
        return self.__consumer_key

    def get_consumer_secret_key(self):
        return self.__consumer_secret

    def get_access_token_key(self):
        return self.__access_token

    def get_access_token_secret_key(self):
        return self.__access_token_secret
