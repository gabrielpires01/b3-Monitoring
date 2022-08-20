import requests

def get_alpha_api(interval, symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey=MZ84TZBQ0JOZNART'

    res = requests.get(url)
    try:
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return data[f'Time Series ({interval})']

def get_alpha_api_last(interval, symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey=MZ84TZBQ0JOZNART'

    res = requests.get(url)
    try:
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return data[f'Time Series ({interval})'][sorted(data[f'Time Series ({interval})'])[-1]]