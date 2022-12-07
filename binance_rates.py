import  requests


def binance_rates(crypto):
    crypto = crypto.text.upper()
    req = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={crypto}USDT')
    response = req.json()
    return response