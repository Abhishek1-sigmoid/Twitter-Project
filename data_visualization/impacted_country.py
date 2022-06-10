from matplotlib import pyplot as plt
import sys
sys.path.append("../")
from queries.impacted_country import impacted_country_weekly


def show_impacts():
    print("Choose any week:"'\n'
          "a-2022-03-21 to 2022-03-28 "'\n'
          "b-2022-03-28 to 2022-04-04 "'\n'
          "c-2022-04-04 to 2022-04-11 "'\n'
          "d-2022-04-11 to 2022-04-18 "'\n'
          "e-2022-04-18 to 2022-04-25 "'\n'
          "f-2022-04-25 to 2022-05-02 "'\n'
          "g-2022-05-02 to 2022-05-09 "'\n'
          "h-2022-05-09 to 2022-05-16 "'\n'
          "i-2022-05-16 to 2022-05-23 ")
    week = input("Enter the week: ")
    impacts = impacted_country_weekly()
    impacts_on_country = impacts[week]
    country = []
    cases = []
    for val in impacts_on_country.items():
        country.append(val[0])
        cases.append(val[1])

    plt.figure(figsize=(30, 30))
    plt.bar(range(len(country)), cases, color='red', align='center')
    plt.title('Rank of Impacted countries from ' + week)
    plt.xticks(range(len(country)), country, rotation='vertical')
    plt.legend()
    plt.xlabel('Country')
    plt.ylabel('Cases')

    plt.savefig('Impacted_country.png')
    plt.show()


if __name__ == '__main__':
    show_impacts()
