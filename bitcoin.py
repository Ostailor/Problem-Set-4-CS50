import requests
import sys

cost = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

try:
    number = float(sys.argv[1])
except (requests.RequestException, ValueError, IndexError):
    if len(sys.argv) == 1:
        print('Missing command-line argument')
        sys.exit()
    elif ValueError:
        print('Command-line argument is not a number')
        sys.exit()
else:
    result = cost['bpi']['USD']['rate_float']
    amount = float(result) * number
    print(f"${amount:,.4f}")
