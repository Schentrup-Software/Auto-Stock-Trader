from alpacaclient import get_closing_stock_prices
from modelbuilder import build_GRU_model
from datatransformations import normalize_data
from datatransformations import denomralize_data
from datatransformations import split_data
 
price = get_closing_stock_prices('AAPL')
print(price)
price = normalize_data(price)
print(price)
x_train, y_train, x_eval = split_data(price, 20)

model = build_GRU_model(x_train, y_train)

x_eval = torch.from_numpy(x_eval).type(torch.Tensor)

print(denomralize_data(model(x_eval)))
