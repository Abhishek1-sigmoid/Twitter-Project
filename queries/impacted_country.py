import requests
import pandas as pd
import sys

sys.path.append('../')

from utils.get_date_range_from_week import get_date_range_from_week

def impacted_country_weekly():
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    data = requests.get(url)
    open('../resources/covid_data.csv', 'wb').write(data.content)
    df = pd.read_csv('../resources/covid_data.csv')
    df = df[(df['date'] >= '2022-04-01') & (df['date'] <= '2022-05-31')]
    df = df[df['iso_code'].str.len() == 3]
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    week_number = df['date'].dt.week
    df['week'] = week_number
    new_df = df[['date', 'week', 'location', 'total_cases']].copy()
    new_df = new_df.dropna()
    result = {}
    for index, row in new_df.iterrows():
        curr_week = str(row['week'])
        start_date, end_date = get_date_range_from_week(2022, curr_week)
        key = str(start_date) + " to " + str(end_date)
        country = row['location']
        cases = row['total_cases']
        if key in result:
            val = result[key]
            if country in val:
                val[country] += cases
            else:
                val[country] = cases
        else:
            result[key] = {country: cases}

    for key, val in result.items():
        val = dict(sorted(val.items(), key=lambda x: x[1], reverse=True))
        result[key] = val

    return result
