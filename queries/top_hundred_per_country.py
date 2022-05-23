import re
from configuration_files.mongodb_connection import DatabaseInfo
from utils.remove_stop_words import preprocess


def top_hundred_per_country():
    db_info = DatabaseInfo()
    collection = db_info.get_database_connection()
    query = [
        {
            "$group": {"_id": {'location': '$location'}}
        }
    ]
    results = collection.aggregate(query)
    countries = []
    country_wise_word = []
    for d in results:
        country = d['_id']['location']
        countries.append(country)
    for country in countries:
        data = collection.find({"location": country})
        text = ""
        for d in data:
            text = text + d['text']
        texts = re.sub('http://\S+|https://\S+', '', text)
        res = preprocess(texts)
        word = {}
        for i in res:
            word[i] = res.count(i)
        results = []
        sorted_tuples = sorted(word.items(), key=lambda item: item[1], reverse=True)
        sorted_tuples = sorted_tuples[0:100]
        for data in sorted_tuples:
            word_count = {'word': data[0], 'count': data[1]}
            results.append(word_count)
        word_dict = {'country': country, 'top_hundred_words': results}
        country_wise_word.append(word_dict)

    country_wise_word_dict = {'country_wise_word': country_wise_word}
    return country_wise_word_dict
