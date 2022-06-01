import sys

sys.path.append('../')

from configuration_files.kafka_details import KafkaInfo

def delete_topics():
    try:
        kafka_details = KafkaInfo()
        admin_client = kafka_details.get_admin_client()
        topic_names = [kafka_details.get_topic()]
        admin_client.delete_topics(topics=topic_names)
        print("Topic Deleted Successfully")
    except Exception as e:
        print(e)

