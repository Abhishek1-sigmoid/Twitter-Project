import json
from datetime import datetime
from tweepy import Stream
from configuration_files.kafka_details import KafkaInfo
from configuration_files.twitter_credentials import TwitterInfo
from utils.get_country_name import get_country_name

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


