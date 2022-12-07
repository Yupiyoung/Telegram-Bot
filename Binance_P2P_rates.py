import requests

def binance_p2p_exchange(currency):
    try:
        currency = currency.text.upper()
        ua = 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
        headers = {
            'authority': 'p2p.binance.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'bnc-uuid': 'c28ba8e7-a1b4-44b1-99df-3501b7ba5e92',
            'c2ctype': 'c2c_merchant',
            'clienttype': 'web',
            'content-type': 'application/json',
            'lang': 'ru',
            'origin': 'https://p2p.binance.com',
            'referer': 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=RUB',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
        }

        buy_json_data = {
            'proMerchantAds': False,
            'page': 1,
            'rows': 10,
            'payTypes': [
                'TinkoffNew',
            ],
            'countries': [],
            'publisherType': None,
            'asset': currency,
            'fiat': 'RUB',
            'tradeType': 'BUY',
        }
        sell_json_data = {
            'proMerchantAds': False,
            'page': 1,
            'rows': 10,
            'payTypes': [
                'TinkoffNew',
            ],
            'countries': [],
            'publisherType': None,
            'asset': currency,
            'fiat': 'RUB',
            'tradeType': 'SELL',
        }
        buy = requests.post(
            'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
            headers=headers,
            json=buy_json_data,
        )
        sell = requests.post(
            'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
            headers=headers,
            json=sell_json_data,
        )
        sell = sell.json()['data'][0]['adv']['price']
        buy = buy.json()['data'][0]['adv']['price']

        return (f'Binance P2P {currency} \nПокупка: {buy}  | Продажа: {sell}')
    except Exception as ex:
        return ('Такой криптовалюты нет на Binance')