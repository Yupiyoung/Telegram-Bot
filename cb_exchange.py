import requests


def cb_exchange(currency):
    currency = currency.text.upper()
    try:
        res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']
        str = ''
        for i in res:
            str += i
        if (currency in str):
            for i in res:
                if (currency == i):
                    rates = res[i]
                    price = rates['Value'] / rates['Nominal']
                    return (f'Курс {i} по ЦБ РФ {price}')
        else:
            return ("Такой валюты нет на ЦБ РФ")
    except Exception as ex:
        return ("Произошла ошибка")
