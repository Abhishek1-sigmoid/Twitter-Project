import requests
import pandas as pd

def economy_impact():
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    data = requests.get(url)
    open('../resources/covid_data.csv', 'wb').write(data.content)
    df = pd.read_csv('../resources/covid_data.csv')
    df = df[(df['date'] >= '2022-04-01') & (df['date'] <= '2022-05-31')]
    df = df[df['iso_code'].str.len() == 3]
    new_df = df[['location', 'gdp_per_capita']].copy()
    new_df = new_df.dropna()
    new_df = new_df.drop_duplicates()
    gdp_list = []
    for index, row in new_df.iterrows():
        location = row['location']
        gdp_per_capita = row['gdp_per_capita']
        gdp_dict = {'country': location, 'gdp_per_capita': gdp_per_capita}
        gdp_list.append(gdp_dict)

    results = {'gdp_country': gdp_list}
    return results
