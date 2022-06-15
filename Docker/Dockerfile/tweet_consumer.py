from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient

'''
consumer_timeout_ms (int, optional) – number of millisecond to throw a timeout exception to the consumer 
if no message is available for consumption. Defaults to -1 (dont throw exception).
'''


def tweet_consumer():
    consumer = KafkaConsumer(
        'tweets',
        bootstrap_servers='192.168.75.90:9092',
        api_version=(2, 5, 0),
        auto_offset_reset='earliest',
        consumer_timeout_ms=10000,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')),
    )

    client = MongoClient('192.168.75.90:27017')
    collection = client.get_database("New_Twitter").get_collection("info")
    for msg in consumer:
        collection.insert_one(msg.value)

tweet_consumer()