import pandas as pd
import alpaca_trade_api as alpaca
from datetime import datetime, time, timedelta
from sklearn.preprocessing import MinMaxScaler
 
from AlpacaPaperTradingSecrects import api_key_id
from AlpacaPaperTradingSecrects import secret_key

class Alpaca(object):

    ALPACA_API_URL = 'https://paper-api.alpaca.markets'

    api = alpaca.REST(api_key_id, secret_key, ALPACA_API_URL)

    def _get_list_of_postions(self, stock_symbol: str):
        return list(filter(lambda x: x.symbol == stock_symbol, self.api.list_positions()))

    def get_closing_stock_prices(self, stock_symbol: str, days_to_look_back: int):
        print("Geting stock prices for " + stock_symbol + "...")

        # Store stock data in a Pandas DataFrame
        result = self.api.get_barset(stock_symbol, 'day', days_to_look_back)
        arr = result[stock_symbol]
        
        variables = vars(arr[0])['_raw'].keys()
        data = pd.DataFrame([[getattr(i,j) for j in variables] for i in arr], columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        data['Date'] = data.apply(lambda x: x['Date'].date(),axis=1)

        return data[['Close']]

    def ensure_position(self, stock_symbol: str):        
        if len(self._get_list_of_postions(stock_symbol)) == 0:
            print('Creating position in ' + stock_symbol)
            self.api.submit_order(stock_symbol, 1, 'buy', 'market', 'day')
        else:
            print('Position already exists for ' + stock_symbol)

    def ensure_no_position(self, stock_symbol: str):
        if len(self._get_list_of_postions(stock_symbol)) > 0:
            print('Selling position in ' + stock_symbol)
            self.api.submit_order(stock_symbol, 1, 'sell', 'market', 'day')
        else:
            print('No position already exists for ' + stock_symbol)
