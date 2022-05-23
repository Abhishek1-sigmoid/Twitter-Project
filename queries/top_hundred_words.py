import re
from configuration_files.mongodb_connection import DatabaseInfo
from utils.remove_stop_words import preprocess


def top_hundred_words():
    db_info = DatabaseInfo()
    collection = db_info.get_database_connection()
    data = collection.find()
    texts = ""
    for d in data:
        texts = texts + d["text"]
    texts = re.sub('http://\S+|https://\S+', '', texts)
    res = preprocess(texts)
    t = {}
    for i in res:
        t[i] = int(res.count(i))
    results = []
    sorted_tuples = sorted(t.items(), key=lambda item: item[1], reverse=True)
    sorted_tuples = sorted_tuples[0:100]
    for data in sorted_tuples:
        word_count = {'word': data[0], 'count': data[1]}
        results.append(word_count)
    word_dict = {'top_hundred_words': results}
    return word_dict
