from bs4 import BeautifulSoup
import requests


def precautionary_measures():
    url_1 = "https://www.who.int/health-topics/coronavirus#tab=tab_2"
    url_2 = "https://www.who.int/westernpacific/emergencies/covid-19/information/transmission-protective-measures"
    precautions = []
    page = requests.get(url_1)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find_all(class_="singleTabWrapper")
    data = data[1].findAll('li')
    for i in data:
        precautions.append(i.text)
    page = requests.get(url_2)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find(id="PageContent_C268_Col00")
    data = data.find(class_="sf-content-block content-block")
    data = data.findAll('li')
    for i in data:
        precautions.append(i.text)
    precautions_dict = {'precautionary_measures': precautions}
    return precautions_dict
