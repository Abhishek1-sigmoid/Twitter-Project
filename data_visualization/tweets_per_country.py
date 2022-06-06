from matplotlib import pyplot as plt
import sys
sys.path.append("../")
from queries.tweets_per_country import tweets_per_country


def show_counts():
    results = tweets_per_country()
    results = results['tweets_per_country']
    country = []
    count = []
    for r in results:
        country.append(r["country"])
        count.append(r["tweet_count"])
    plt.figure(figsize=(30,30))
    plt.bar(range(len(country)), count, color='green', align='center')
    plt.title('Tweets per country')
    plt.xticks(range(len(country)), country, rotation='vertical')
    plt.legend()
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.autoscale()
    plt.savefig('Tweets_per_country.png')
    plt.show()


if __name__ == '__main__':
    show_counts()
