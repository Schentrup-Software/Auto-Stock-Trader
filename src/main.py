from datetime import date

from predictor import predict_stock
from stocksymbols import get_stock_symbols
from alpacaclient import Alpaca

today = date.today()
print("Starting todays run:", today)

stock_symbols = get_stock_symbols()
alpaca = Alpaca()

for stock_symbol in stock_symbols:
    try:
        yesterdays_price, projected_price = predict_stock(stock_symbol, 1000)
        print('Yesterdays price: ' + str(yesterdays_price))
        print('Todays projected price: ' + str(projected_price))
        if yesterdays_price < projected_price:
            alpaca.ensure_position(stock_symbol)
        else:
            alpaca.ensure_no_position(stock_symbol)
    except Exception as e:
        print('Execption caught while trying to evaluate ' + stock_symbol)
        print(e)

