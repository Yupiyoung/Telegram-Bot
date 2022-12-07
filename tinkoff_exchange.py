import requests

def tinkoff_exchange(currency):
    try:
        currency = currency.text.upper()
        req = requests.get(f'https://api.tinkoff.ru/v1/currency_rates?from={currency}&to=RUB')
        buy = req.json()['payload']['rates'][1]['buy']
        sell = req.json()['payload']['rates'][1]['sell']
        return (f'Тинькофф {currency} \nПокупка: {buy}  | Продажа: {sell}')
    except Exception as ex:
        return ("Такой валюты нет в Тинькофф")