from coinbaseauth import CoinbaseExchangeAuth
import requests


class coinpy(object):

    def __init__(self, api_key, api_secret, passcode):
        self.api_url = 'https://api.pro.coinbase.com/'
        self.auth = CoinbaseExchangeAuth(api_key, api_secret, passcode)

    
    def get_accounts(self,account_id=''):
        # Get account information
        r = requests.get(self.api_url + 'accounts/' + account_id, auth=self.auth)
        print(r.json())
        return r.json()

    def get_account_history(self, account_id):
        # Get account information in detail
        r = requests.get(self.api_url + 'accounts/' +
                         account_id + '/ledger', auth=self.auth)
        print(r.json())
        return r.json()

    def get_account_hold(self, account_id):
        # Get account information in detail
        r = requests.get(self.api_url + 'accounts/' +
                         account_id + '/holds', auth=self.auth)
        print(r.json())
        return r.json()

    def list_fills(self):
        # Get a list of recent fills of the API key's profile.
        r = requests.get(self.api_url + 'fills', auth=self.auth)
        print(r.json())
        return r.json()
