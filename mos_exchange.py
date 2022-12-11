import  requests
from datetime import datetime
import json

def mos_exchange(currency):
    currency = currency.text.upper()
    if (currency == "USD"):
        req = requests.get(
            f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/USD000000TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={datetime.now().year}-{datetime.now().month}-{datetime.now().day - 1}')
        response = req.text
        response = response[14:]
        response = response[:-1]
        response = json.loads(response)
        if (not response[1]['history']):
            return ('На данный момент нет актульного курса')
        else:
            response = response[1]['history'][0]['CLOSE']
            return (f'МосБиржа {currency} \nПокупка: {response}')
    elif (currency == "EUR"):
        req = requests.get(
            f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/EUR_RUB__TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={datetime.now().year}-{datetime.now().month}-{datetime.now().day - 1}')
        response = req.text
        response = response[14:]
        response = response[:-1]
        response = json.loads(response)
        if (not response[1]['history']):
            return ('На данный момент нет актульного курса')
        else:
            response = response[1]['history'][0]['CLOSE']
            return (f'МосБиржа {currency} \nПокупка: {response}')
    elif (currency == "CNY"):
        req = requests.get(
            f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/CNY000000TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={datetime.now().year}-{datetime.now().month}-{datetime.now().day - 1}')
        response = req.text
        response = response[14:]
        response = response[:-1]
        response = json.loads(response)
        if (not response[1]['history']):
            return ('На данный момент нет актульного курса')
        else:
            response = response[1]['history'][0]['CLOSE']
            return (f'МосБиржа {currency} \nПокупка: {response}')
    elif (currency == "BYN"):
        req = requests.get(
            f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/BYNRUB_TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={datetime.now().year}-{datetime.now().month}-{datetime.now().day - 1}')
        response = req.text
        response = response[14:]
        response = response[:-1]
        response = json.loads(response)
        if (not response[1]['history']):
            return ('На данный момент нет актульного курса')
        else:
            response = response[1]['history'][0]['CLOSE']
            return (f'МосБиржа {currency} \nПокупка: {response}')
    elif (currency == "TRY"):
        req = requests.get(
            f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/TRYRUB_TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={datetime.now().year}-{datetime.now().month}-{datetime.now().day - 1}')
        response = req.text
        response = response[14:]
        response = response[:-1]
        response = json.loads(response)
        if (not response[1]['history']):
            return ('На данный момент нет актульного курса')
        else:
            response = response[1]['history'][0]['CLOSE']
            return (f'МосБиржа {currency} \nПокупка: {response}')
    else:
        return ("Такой валюты нет на МосБирже")
