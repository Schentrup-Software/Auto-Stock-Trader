import torch
from sklearn.preprocessing import MinMaxScaler

from alpacaclient import Alpaca
from modelbuilder import build_GRU_model
from datatransformations import split_data

def predict_stock(stock_symbol: str, days_to_look_back: int):
    price = Alpaca().get_closing_stock_prices(stock_symbol, days_to_look_back)
    yesterdays_price = price['Close'][days_to_look_back - 1]

    scaler = MinMaxScaler(feature_range=(-1, 1))
    price['Close'] = scaler.fit_transform(price['Close'].values.reshape(-1,1))

    x_train, y_train, x_eval = split_data(price, 20)

    model = build_GRU_model(x_train, y_train)

    x_eval = torch.from_numpy(x_eval).type(torch.Tensor)

    print("Evaluating..")
    result = scaler.inverse_transform(model(x_eval).detach().numpy())
    result = result[-1, -1]
    print("Projected stock price for " + stock_symbol + ": " + str(result))
    
    return yesterdays_price, result
