from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient


class KafkaInfo:
    def __init__(self):
        self.__topic = "tweets"
        self.__bootstrap_server = "localhost:9092"

    def get_topic(self):
        return self.__topic

    def get_server(self):
        return self.__bootstrap_server

    def get_producer(self):
        return KafkaProducer(bootstrap_servers=self.__bootstrap_server)

    def get_consumer(self):
        return KafkaConsumer(bootstrap_servers=self.__bootstrap_server)

    def get_admin_client(self):
        return KafkaAdminClient(bootstrap_servers=self.__bootstrap_server)
