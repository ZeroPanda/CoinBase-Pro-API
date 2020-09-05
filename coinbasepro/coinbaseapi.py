from coinbaseauth import CoinbaseExchangeAuth
import requests
import json

class coinpy(object):

    def __init__(self, api_key, api_secret, passcode):
        self.api_url = 'https://api.pro.coinbase.com/'
        self.auth = CoinbaseExchangeAuth(api_key, api_secret, passcode)

        self.websocketURI = 'wss://ws-feed.pro.coinbase.com'
        self.session = requests.Session()

    
    ### All the GET requuests ###

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

    def list_orders(self, order_id=''):
        # Get order information in detail
        r = requests.get(self.api_url + 'orders/' +
                         order_id, auth=self.auth)
        print(r.json())
        return r.json()

    def list_fills(self):
        # Get a list of recent fills of the API key's profile.
        r = requests.get(self.api_url + 'fills', auth=self.auth)
        print(r.json())
        return r.json()

    def exchange_limits(self):
        # Get Current Exchange Limits
        r = requests.get(
            self.api_url + '/users/self/exchange-limits', auth=self.auth)
        print(r.json())
        return r.json()

    def list_deposits(self,transfer_id=''):
        # Get trnasfers
        try:
            r = requests.get(self.api_url + 'transfers' + transfer_id, auth=self.auth)
        except:
            r = requests.get(self.api_url + 'transfers/:' +
                             transfer_id, auth=self.auth)
        print(r.json())
        return r.json()

    def payment_method(self):
        # Get the payment method
        r = requests.get(
            self.api_url + 'payment-methods', auth=self.auth)
        print(r.json())
        return r.json()

    def coinbase_accounts(self):
        # Get the coinbase account
        r = requests.get(
            self.api_url + 'coinbase-accounts', auth=self.auth)
        print(r.json())
        return r.json()

    def current_fees(self):
        # Get the current fees
        r = requests.get(
            self.api_url + 'fees', auth=self.auth)
        print(r.json())
        return r.json()

    def get_profiles(self,profile_id=''):
        # List your profiles
        r = requests.get(
            self.api_url + 'profiles/' + profile_id, auth=self.auth)
        print(r.json())
        return r.json()

    def trailing_volume(self):
        # Get the trailing volume
        r = requests.get(
            self.api_url + 'users/self/trailing-volume', auth=self.auth)
        print(r.json())
        return r.json()

    def margin(self,para):
        # Get margin profile_information/buying_power/withdrawal_power/withdrawal_power_all/exit_plan/liquidation_history/position_refresh_amounts/status
        try:
            r = requests.get(
                self.api_url + 'margin/' + para, auth=self.auth)
            print(r.json())
            return r.json()
        except NameError:
            pass
        
    def oracle(self):
        # get the open oracle values
        r = requests.get(
            self.api_url + 'oracle', auth=self.auth)
        print(r.json())
        return r.json()

    ## Get the market data ##
    ## Requires websocket ##

    def get_products(self):
        # Get all the product information
        r = requests.get(self.api_url + 'products' , auth=self.auth)
        print(r.json())
        return r.json()

    def get_product_info(self, product_id,para=''):
        # Get product information , book/ticker/trades/candles/stats
        try:
            r = requests.get(self.api_url + 'products/' + product_id +'/' + para,auth=self.auth)
            print(r.json())
            return r.json()
        except NameError:
            pass

    def get_currencies(self):
        # Get currency information
        r = requests.get(self.api_url + 'currencies', auth=self.auth)
        print(r.json())
        return r.json()

    def get_time(self):
        # Get the API server time
        r = requests.get(self.api_url + 'time', auth=self.auth)
        print(r.json())
        return r.json()

    ### POST ###

    def payment_deposit(self, amountQTY, currencyQTY, paymentMID):
        # post deposit/payment-method
        data = {
            "amount": str(amountQTY),
            "currency": str(currencyQTY),
            "payment_method_id": str(paymentMID)
        }
        r = requests.post(
            self.api_url + 'deposits/payment-method', auth=self.auth, json=data)
        print(r.json())
        return r.json()

    def account_deposit(self, amountQTY, currencyQTY, coinbaseAID):
        # post deposits/coinbase-account
        data = {
            "amount": str(amountQTY),
            "currency": str(currencyQTY),
            "coinbase_account_id": str(coinbaseAID)
        }
        r = requests.post(
            self.api_url + 'deposits/coinbase-account', auth=self.auth, json=data)
        print(r.json())
        return r.json()

    def payment_withdrawal(self, amountQTY, currencyQTY, paymentMID):
        # post withdrawals/payment-method
        data = {
            "amount": str(amountQTY),
            "currency": str(currencyQTY),
            "payment_method_id": str(paymentMID)
        }
        r = requests.post(
            self.api_url + 'withdrawals/payment-method', auth=self.auth, json=data)
        print(r.json())
        return r.json()

    def account_withdrawal(self, amountQTY, currencyQTY, coinbaseAID):
        # post withdrawals/coinbase-account
        data = {
            "amount": str(amountQTY),
            "currency": str(currencyQTY),
            "coinbase_account_id": str(coinbaseAID)
        }
        r = requests.post(
            self.api_url + 'withdrawals/coinbase-account', auth=self.auth, json=data)
        print(r.json())
        return r.json()

    def crypto_withdrawal(self, amountQTY, currencyQTY, cryptoAddress):
        # post withdrawals/crypto
        data = {
            "amount": str(amountQTY),
            "currency": str(currencyQTY),
            "crypto_address": str(cryptoAddress)
        }
        r = requests.post(
            self.api_url + 'withdrawals/crypto', auth=self.auth, json=data)
        print(r.json())
        return r.json()

    def conversions(self, fromQTY, toQTY, amountQTY):
        # post conversions
        data = {
            "from": str(fromQTY),
            "to": str(toQTY),
            "amount": str(amountQTY)
        }
        r = requests.post(
            self.api_url + 'conversions', auth=self.auth, json=data)
        print(r.json())
        return r.json()

    def get_reports(self,report_type,start_date,end_date):
        # post the reports
        data = {
            "type": str(report_type),
            "start_date": str(start_date),
            "end_date": str(end_date)
        }
        r = requests.post(self.api_url + 'reports', auth=self.auth,json=data)
        print(r.json())
        return r.json()

    def profile_transfer(self, fromQTY, toQTY,currencyQTY, amountQTY):
        # post profile/transfer
        data = {
            "from": str(fromQTY),
            "to": str(toQTY),
            "currency": str(currencyQTY),
            "amount": str(amountQTY)
        }
        r = requests.post(
            self.api_url + 'profiles/transfer', auth=self.auth, json=data)
        print(r.json())
        return r.json()

    def place_order(self, **kwarg):
        # post limit orders
        '''
        client.place_order(size: "0.01", price: "0.100", side: "buy", product_id:  "BTC-USD")
        '''
        r = requests.post(
            self.api_url + 'orders', auth=self.auth, json=kwarg)
        print(r.json())
        return r.json()

    ### DELETE ###

    def delete_order(self, order_id=''):
        # Post cancel order
        try:
            r = requests.post(self.api_url + 'orders/' +
                              order_id, auth=self.auth)
            print(r.json())
            return r.json()
        except NameError:
            pass

    def delete_order_coid(self, client_oid=''):
        # Post cancel order with client oid
        try:
            r = requests.post(self.api_url + 'orders/client:' +
                              client_oid, auth=self.auth)
            print(r.json())
            return r.json()
        except NameError:
            pass


    
