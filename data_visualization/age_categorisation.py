import numpy as np
from matplotlib import pyplot as plt
import sys
sys.path.append("../")

from queries.age_categorisation import age_categorisation


def show_age_categorisation():
    age_categorisation_info = age_categorisation()
    age_categorisation_info = age_categorisation_info['age_categorisation_data']
    country = []
    b_45 = []
    b_55 = []
    b_65 = []
    b_75 = []
    b_85 = []
    a_85 = []
    for r in age_categorisation_info:
        country.append(r["country"])
        for d in r["death % by age-group"]:
            print(d)
            b_45.append(d["age_0_to_44"])
            b_55.append(d["age_45_to_54"])
            b_65.append(d["age_55_to_64"])
            b_75.append(d["age_65_to_74"])
            b_85.append(d["age_75_to_84"])
            a_85.append(d["age_above_85"])

    w = 0.075
    bar1 = np.arange(len(country))
    bar2 = [i + w for i in bar1]
    bar3 = [i + w for i in bar2]
    bar4 = [i + w for i in bar3]
    bar5 = [i + w for i in bar4]
    bar6 = [i + w for i in bar5]
    plt.figure(figsize=(30, 30))
    y = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    plt.bar(bar1, b_45, w, label="0-44")
    plt.bar(bar2, b_55, w, label="45-54")
    plt.bar(bar3, b_65, w, label="55-64")
    plt.bar(bar4, b_75, w, label="65-74")
    plt.bar(bar5, b_85, w, label="75-84")
    plt.bar(bar6, a_85, w, label="85+")
    plt.xlabel('country')
    plt.ylabel('Percent of death')
    plt.title("Death analysis of different age group")
    plt.yticks(y, y)
    plt.xticks(bar1+3*w, country, rotation='vertical')
    plt.legend()
    plt.autoscale()
    plt.margins()
    plt.savefig('Age.png')
    plt.show()


if __name__ == '__main__':
    show_age_categorisation()
