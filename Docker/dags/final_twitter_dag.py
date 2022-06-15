from airflow import DAG
from datetime import timedelta
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient
from airflow.operators.python import PythonOperator
from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient
import json
from datetime import datetime
from geopy.geocoders import Nominatim
from tweepy import Stream
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


class KafkaInfo:
    def __init__(self):
        self.__topic = "tweets"
        self.__bootstrap_server = "192.168.29.24:9092"

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


def get_country_name(place):
    nom = Nominatim(user_agent="My-Application")
    location = nom.geocode(place, addressdetails=True)
    if location is None:
        return ""
    if 'country' in location.raw['address'].keys():
        return location.raw['address']['country']
    else:
        return ""



def delete_topics():
    try:
        kafka_details = KafkaInfo()
        admin_client = kafka_details.get_admin_client()
        topic_names = [kafka_details.get_topic()]
        admin_client.delete_topics(topics=topic_names)
        print("Topic Deleted Successfully")
    except Exception as e:
        print(e)


def tweet_consumer():
    consumer = KafkaConsumer(
        'tweets',
        bootstrap_servers='192.168.29.24:9092',
        api_version=(2, 5, 0),
        auto_offset_reset='earliest',
        consumer_timeout_ms=10000,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')),
    )

    client = MongoClient('192.168.29.24:27017')
    collection = client.get_database("New_Twitter").get_collection("info")
    for msg in consumer:
        collection.insert_one(msg.value)
        print("done")


twitter_details = TwitterInfo()
kafka_details = KafkaInfo()
producer = kafka_details.get_producer()
count = 0


class Listener(Stream):
    def on_data(self, raw_data):
        global count
        count += 1
        data = json.loads(raw_data)
        info = dict()
        info['id'] = data['id']
        info['text'] = data['text']
        dtime = data['created_at']
        new_datetime = datetime.strftime(datetime.strptime(dtime, '%a %b %d %H:%M:%S +0000 %Y'), '%d-%m-%Y ')
        info['created_at'] = new_datetime
        info['location'] = get_country_name(data['user']['location'])
        info['name'] = data['user']['name']
        info['followers_count'] = data['user']['followers_count']
        info['retweet_count'] = data['retweet_count']
        print(info)
        print(count)
        producer.send(kafka_details.get_topic(), json.dumps(info).encode('utf-8'))
        if count == 20:
            self.disconnect()

    def disconnect(self):
        if self.running is False:
            return
        self.running = False

    def on_closed(self, response):
        print("Stream closed")


def get_twitter_data():
    consumer_key = twitter_details.get_consumer_key()
    consumer_secret = twitter_details.get_consumer_secret_key()
    access_token = twitter_details.get_access_token_key()
    access_token_secret = twitter_details.get_access_token_secret_key()

    myStream = Listener(consumer_key, consumer_secret, access_token, access_token_secret)
    myStream.filter(track=['#covid, #corona'])

# get_twitter_data()

default_args = {
    "owner": "Danish",
    "depends_on_past": False,
    "start_date": datetime(2022, 6, 13),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "catchup": False,
    "retry_delay": timedelta(minutes=1)
}

# get_twitter_data()
# tweet_consumer()

dag = DAG("Twitter_Project3.0", default_args=default_args, schedule_interval="0 9 * * *", catchup= False)
t1 = PythonOperator(task_id='twitter_producer', python_callable=get_twitter_data, dag=dag)
t2 = PythonOperator(task_id='twitter_consumer', python_callable=tweet_consumer, dag=dag)
t3 = PythonOperator(task_id='clear_topic', python_callable=delete_topics, dag=dag)

t1 >> t2 >> t3
