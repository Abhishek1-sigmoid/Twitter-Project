from matplotlib import pyplot as plt
import sys
sys.path.append("../")

from queries.economy_impact import economy_impact


def show_gdp():
    gdp_country_info = economy_impact()
    gdp_country_info = gdp_country_info['gdp_country']
    country = []
    gdp_per_capita = []
    for r in gdp_country_info:
        country.append(r["country"])
        gdp_per_capita.append(r["gdp_per_capita"])
    plt.figure(figsize=(30, 30))
    plt.bar(range(len(country)), gdp_per_capita, color='purple', align='center')
    plt.title('GDP analysis')
    plt.xticks(range(len(country)), country, rotation='vertical')
    plt.legend()
    plt.xlabel('Country')
    plt.ylabel('GDP')
    plt.autoscale()
    plt.savefig('Economy_impact.png')
    plt.show()


if __name__ == '__main__':
    show_gdp()
