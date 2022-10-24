import requests
import json
import sys


def exchange_rate_to_pln(currency='eur'):
    """Fetches current rate of given currency to PLN from NBP.

    Keyword arguments
        currency -- Symbol of currency to fetch the rate for (default = "eur")
    """
    result = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/')

    code = result.status_code
    if code == 404:
        return print(f'{currency} is not a valid currency.')
    elif code != 200:
        return print(f'Error: {code}')

    data = json.loads(result.text)
    rate = data["rates"][0]["mid"]

    output = {
        "currency": currency,
        "price": rate,
    }

    print(json.dumps(output))


if len(sys.argv) > 1:
    currencySymbol = sys.argv[1]
    exchange_rate_to_pln(currency=currencySymbol)
else:
    exchange_rate_to_pln()
