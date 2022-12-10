import alpaca_trade_api as tradeapi
import numpy as np
import time

SEC_KEY = ''
PUB_KEY = ''
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)

symb = "SPY"