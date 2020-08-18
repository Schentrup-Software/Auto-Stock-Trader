from sklearn.preprocessing import MinMaxScaler
import numpy as np

def normalize_data(price):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    price['Close'] = scaler.fit_transform(price['Close'].values.reshape(-1,1))
    return price

def denomralize_data(price):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    return scaler.inverse_transform(price.detach().numpy())

def split_data(stock, lookback):
    data_raw = stock.to_numpy() # convert to numpy array
    data = []
    
    # create all possible sequences of length seq_len
    for index in range(len(data_raw) - lookback): 
        data.append(data_raw[index: index + lookback])
 
    data = np.array(data)
 
    x_train = data[:,:-1,:]
    y_train = data[:,-1,:]
    x_eval = data[-1:,:,:]

    return [x_train, y_train, x_eval]
