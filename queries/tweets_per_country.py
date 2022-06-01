import sys

sys.path.append('../')

from configuration_files.mongodb_connection import DatabaseInfo


def tweets_per_country():
    query = [
        {
            "$match": {'location': {"$ne": ""}}
        },
        {
            "$group": {"_id": {'location': '$location'}, 'total': {'$sum': 1}}
        },
        {
            "$sort": {"total": -1}
        }
    ]
    db_info = DatabaseInfo()
    results = []
    collection = db_info.get_database_connection()
    data = collection.aggregate(query)
    for d in data:
        country_count = {'country': d['_id']['location'], 'tweet_count': d['total']}
        results.append(country_count)
    tweets_country = {'tweets_per_country': results}
    return tweets_country
