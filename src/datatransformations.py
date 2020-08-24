import numpy as np

def split_data(stock, lookback):
    print("Spliting data...")
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
