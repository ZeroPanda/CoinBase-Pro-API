# CoinBase-Pro-API
Python API for CoinBase Pro (reference: https://docs.pro.coinbase.com/?python)
To run the API, activate API on your CoinBase Pro account.
get and copy `API KEY` , `API SECRET` and `PASSCODE`.
Install the API setup.
Import `coinpy` from `coinbaseapi`.
```
from coinbasepro.coinbaseapi import coinpy
Coinbase = coinpy(API_KEY, API_SECRET, PASSCODE)
```
```
# Example: get all accounts info
coinpy.get_accounts()
```
