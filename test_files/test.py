import unittest
import requests

class TestApis(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        print('\nSetup Class')

    @classmethod
    def teardown_class(cls):
        print("\nTearing Down Class")

    def test_api_tweets_per_country(self):
        response = requests.get('http://127.0.0.1:5000/api/tweets_per_country')
        assert response.status_code == 200

    def test_api_tweets_per_country_daily(self):
        response = requests.get('http://127.0.0.1:5000/api/tweets_per_country_daily')
        assert response.status_code == 200

    def test_api_top_hundred_words(self):
        response = requests.get('http://127.0.0.1:5000/api/top_hundred_words')
        assert response.status_code == 200

    def test_api_top_hundred_per_country(self):
        response = requests.get('http://127.0.0.1:5000/api/top_hundred_per_country')
        assert response.status_code == 200

    def test_api_precautionary_measures(self):
        response = requests.get('http://127.0.0.1:5000/api/precautions')
        assert response.status_code == 200

    def test_api_donations(self):
        response = requests.get('http://127.0.0.1:5000/api/donations')
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
