import datetime

def get_date_range_from_week(p_year, p_week):
    first_day_of_week = datetime.datetime.strptime(f'{p_year}-W{int(p_week) - 1}-1', "%Y-W%W-%w").date()
    last_day_of_week = first_day_of_week + datetime.timedelta(days=7)
    return first_day_of_week, last_day_of_week
