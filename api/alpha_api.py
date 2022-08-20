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
 
def check_last_alpha_api(interval, symbol, top, bottom, to_email):
    last_data = get_alpha_api_last(interval, symbol)
    closed_data = last_data['4. close']

    if closed_data > top:
        send_mail(
            'Sell Actives',
            f'Is time to sell yours actives from {symbol}: it value is {closed_data}',
            f'{from_email}',
            [f'{from_email}'],
            fail_silently=False,
        )
    elif closed_data < bottom:
        send_mail(
            'Buy Actives',
            f'Is time to buy actives from {symbol}: it value is {closed_data}',
            f'{from_email}',
            [f'{from_email}'],
            fail_silently=False,
        )
