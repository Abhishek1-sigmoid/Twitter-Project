from nltk.corpus import stopwords
import gensim

stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're/', 'edu', 'use'])


def preprocess(texts):
    result = []
    for token in gensim.utils.simple_preprocess(texts):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(token)

    return result
