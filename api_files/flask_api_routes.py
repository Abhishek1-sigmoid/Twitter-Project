import sys
from flask import Flask, jsonify

sys.path.append('../')

from queries.donations import donations_per_country
from queries.precautionary_measures import precautionary_measures
from queries.top_hundred_per_country import top_hundred_per_country
from queries.top_hundred_words import top_hundred_words
from queries.tweets_per_country import tweets_per_country
from queries.tweets_per_country_daily import tweets_per_country_daily_basis

app = Flask('my app')


@app.route('/api/tweets_per_country', methods=['GET'])
def api_tweets_per_country():
    data = tweets_per_country()
    return jsonify(data)


@app.route('/api/tweets_per_country_daily', methods=['GET'])
def api_tweets_per_country_daily():
    data = tweets_per_country_daily_basis()
    return jsonify(data)


@app.route('/api/top_hundred_words', methods=['GET'])
def api_top_hundred_words():
    data = top_hundred_words()
    return jsonify(data)


@app.route('/api/top_hundred_per_country', methods=['GET'])
def api_top_hundred_per_country():
    data = top_hundred_per_country()
    return jsonify(data)


@app.route('/api/precautions', methods=['GET'])
def api_precautionary_measures():
    data = precautionary_measures()
    return jsonify(data)


@app.route('/api/donations', methods=['GET'])
def api_donations():
    data = donations_per_country()
    return jsonify(data)


if __name__ == '__main__':
    app.run()
