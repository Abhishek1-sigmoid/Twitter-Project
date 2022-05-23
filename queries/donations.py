from bs4 import BeautifulSoup
import requests

def donations_per_country():
    url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/donors-and-partners/funding"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")
    data = soup.find(id="PageContent_C003_Col01")
    data = data.findAll(class_="sf-content-block content-block")
    data = data[2]
    data = data.findAll('tr')
    donation_info = []
    for d in data:
        donation_data = d.findAll('td')
        donation_country = donation_data[0].text
        donation_amount = donation_data[1].text
        donation_dict = {'donor': donation_country, 'donation_amount': donation_amount}
        donation_info.append(donation_dict)

    donation_info = donation_info[1:len(donation_info)-1]
    donation_info_dict = {'donations_info': donation_info}
    return donation_info_dict
