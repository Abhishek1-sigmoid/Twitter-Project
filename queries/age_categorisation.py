from bs4 import BeautifulSoup


def age_categorisation():
    html_data = open('../resources/covid-19_age_categorisation_data.html', 'r')
    html_content = html_data.read()
    soup = BeautifulSoup(html_content, "html.parser")
    data = soup.find_all('ol')
    data = data[1].next_sibling
    data = data.findAll('tr')
    data = data[3:]
    age_category = []
    for row in data:
        curr_data = row.find_all('td')
        country = curr_data[0].text
        age_0_to_44 = curr_data[3].text
        age_45_to_54 = curr_data[4].text
        age_55_to_64 = curr_data[5].text
        age_65_to_74 = curr_data[6].text
        age_75_to_84 = curr_data[7].text
        age_above_85 = curr_data[8].text
        curr_dict = {'country': country, 'death % by age-group': [{'age_0_to_44': age_0_to_44,
                                                                   'age_45_to_54': age_45_to_54,
                                                                   'age_55_to_64': age_55_to_64,
                                                                   'age_65_to_74': age_65_to_74,
                                                                   'age_75_to_84': age_75_to_84,
                                                                   'age_above_85': age_above_85}]}
        age_category.append(curr_dict)
    results = {'age_categorisation_data': age_category}
    return results
