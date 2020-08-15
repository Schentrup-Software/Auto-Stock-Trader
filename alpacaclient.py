import pandas as pd
import alpaca_trade_api as alpaca
from datetime import datetime, time, timedelta
from sklearn.preprocessing import MinMaxScaler
 
from AlpacaPaperTradingSecrects import api_key_id
from AlpacaPaperTradingSecrects import secret_key

def get_closing_stock_prices(stock_symbol):
    api = alpaca.REST(api_key_id, secret_key, 'https://paper-api.alpaca.markets')

    # Store stock data in a Pandas DataFrame
    result = api.get_barset(stock_symbol, 'day', 1000)
    arr = result[stock_symbol]
    
    variables = vars(arr[0])['_raw'].keys()
    data = pd.DataFrame([[getattr(i,j) for j in variables] for i in arr], columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    data['Date'] = data.apply(lambda x: x['Date'].date(),axis=1)

    return data[['Close']]
