import requests
import json
import sys


def get_euro_to_pln_exchange_rate(currency='eur'):
    """Fetches current rate of given currency to PLN from NBP.

    Keyword arguments
        currency -- Symbol of currency to fetch the rate for (default = "eur")
    """
    result = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/'.format(currency=currency))

    if result.status_code != 200:
        print(f'{currency} is not a valid symbol')
        return

    data = json.loads(result.text)
    rate = data["rates"][0]["mid"]

    print(f'{currency.upper()}/PLN rate : {rate}')


if len(sys.argv) > 1:
    currencySymbol = sys.argv[1]
    get_euro_to_pln_exchange_rate(currency=currencySymbol)
else:
    get_euro_to_pln_exchange_rate()


