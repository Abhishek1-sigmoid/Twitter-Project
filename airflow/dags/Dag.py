from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


from twitter_files.delete_topic import delete_topics
from twitter_files.tweet_consumer import tweet_consumer
from twitter_files.tweet_producer import get_twitter_data

default_args = {
    "owner": "Abhishek",
    "depends_on_past": False,
    "start_date": datetime(2022, 5, 18),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

dag = DAG("Twitter_Project", default_args=default_args, schedule_interval="0 6 * * *")

t1 = PythonOperator(task_id='producer', python_callable=get_twitter_data, dag=dag)
t2 = PythonOperator(task_id='consumer', python_callable=tweet_consumer, dag=dag)
t3 = PythonOperator(task_id='clear_topic', python_callable=delete_topics, dag=dag)

t1 >> t2 >> t3
