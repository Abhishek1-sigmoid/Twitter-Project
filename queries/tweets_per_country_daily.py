from configuration_files.mongodb_connection import DatabaseInfo


def tweets_per_country_daily_basis():
    query = [
        {
            "$match": {'location': {"$ne": ""}}
        },
        {
            "$group": {"_id": {'date': "$created_at", 'country': '$location'}, "count": {'$sum': 1}}
        },
        {
            "$sort": {'_id.date': 1}
        }
    ]

    db_info = DatabaseInfo()
    collection = db_info.get_database_connection()
    data = collection.aggregate(query)
    tweet_per_country = {}
    results = []
    for d in data:
        date = d['_id']['date']
        if date in tweet_per_country:
            tweet_per_country[date].append({'country': d['_id']['country'], 'count': d['count']})
        else:
            tweet_per_country[date] = [{'country': d['_id']['country'], 'count': d['count']}]
    for d in tweet_per_country:
        results.append({'date': d, 'tweets_per_country': tweet_per_country[d]})
    tweet_per_country_daily = {'tweets_per_country_daily': results}
    return tweet_per_country_daily
