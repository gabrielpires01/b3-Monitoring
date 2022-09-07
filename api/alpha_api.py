import requests
from django.core.mail import send_mail

def get_alpha_api(interval, symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey=MZ84TZBQ0JOZNART'

    res = requests.get(url)
    try:
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    if "Error Message" in data:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=MZ84TZBQ0JOZNART'
        res = requests.get(url)

        try:
            res.raise_for_status()
            data = res.json()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return data['Time Series (Daily)']

    return data[f'Time Series ({interval})']

def get_alpha_api_last(interval, symbol):
    data = get_alpha_api(interval, symbol)
    return data[sorted(data)[-1]]
