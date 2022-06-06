from matplotlib import pyplot as plt
import sys
sys.path.append("../")
from queries.donations import donations_per_country


def show_donations():
    donation_info = donations_per_country()
    donation_info = donation_info['donations_info']
    donar = []
    amount = []
    for r in donation_info:
        donar.append(r["donor"])
        amount.append(r["donation_amount"])
    plt.figure(figsize=(30,30))
    plt.bar(range(len(donar)), amount, color='green', align='center')
    plt.title('Total donations')
    plt.xticks(range(len(donar)), donar, rotation='vertical')
    plt.legend()
    plt.xlabel('Donar')
    plt.ylabel('Donation')
    plt.autoscale()
    plt.savefig('Donations.png')
    plt.show()


if __name__ == '__main__':
    show_donations()
