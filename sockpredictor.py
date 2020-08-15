!pip install alpaca-trade-api
!pip install pandas

from alpacaclient import get_closing_stock_prices
from modelbuilder import build_GRU_model
from modelevaluator import evaluate_model
import datatransformations
 
price = get_closing_stock_prices('AAPL')

price = normalize_data(price)

x_train, y_train, x_eval = split_data(price, 20)

model = build_GRU_model(x_train, y_train)

x_eval = torch.from_numpy(x_eval).type(torch.Tensor)

print(denomralize_data(model(x_eval)))
