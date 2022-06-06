from matplotlib import pyplot as plt
import sys
sys.path.append("../")
from queries.tweets_per_country_daily import tweets_per_country_daily_basis


def show_counts():
    result = tweets_per_country_daily_basis()
    result = result['tweets_per_country_daily']
    country = []
    count = []
    date = ""
    for r in result:
        date = r["date"]
        data = r["tweets_per_country"]
        country = []
        count = []
        for d in data:
            country.append(d["country"])
            count.append(d["count"])
    plt.figure(figsize=(30,30))
    plt.bar(range(len(country)), count, color='green', align='center')
    plt.title('Tweets per country on '+date)
    plt.xticks(range(len(country)), country, rotation='vertical')
    plt.legend()
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.autoscale()
    plt.savefig('Tweets_per_country_daily.png')
    plt.show()


if __name__ == '__main__':
    show_counts()
