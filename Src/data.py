from alpha_vantage.timeseries import TimeSeries
from datetime import date, datetime, timedelta

def get_series_daily(symbol, _key):
    ts = TimeSeries(key=_key)

    try:
        data, meta_data = ts.get_daily(symbol)
        return data, meta_data
    except Exception as e:
        print('O program encontrou um erro: {erro}'.format(erro = e))

def get_closing_values(data):
    closing_values = {}
    for date in data.keys():
        closing_values[date] = float(data[date]['4. close'])

    return closing_values

def last_week_dates():
    today = datetime.now()
    last_sunday = today - timedelta(days=((datetime.now().isoweekday() + 1) % 7))
    last_week_start = last_sunday - timedelta(days = 6)
    last_week_dates = []

    for i in range(0, 6):
        last_week_dates.append((last_week_start + timedelta(days=i)).date())

    return last_week_dates

def filter_by_dates(closing_values, date_list):
    filtered_values = {}

    for date in closing_values.keys():
        datetime_obj = datetime.strptime(date, '%Y-%m-%d').date()
        if datetime_obj in date_list:
            filtered_values[date] = closing_values[date]

    return filtered_values

def get_default_values(symbol, API_KEY):
    _last_week_dates = last_week_dates()

    series_daily, meta_data = get_series_daily(symbol, API_KEY)
    
    closing_values = get_closing_values(series_daily)

    last_week_values = filter_by_dates(closing_values, _last_week_dates)

    return last_week_values