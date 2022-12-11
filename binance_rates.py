import requests


def binance_rates(crypto):
    crypto = crypto.text.upper()
    try:
        req = requests.get(
            f'https://api.binance.com/api/v3/ticker/price?symbol={crypto}USDT')
        response = req.json()
        if (response.get("code")):
            if (response.get("code") == -1100):
                return ("Вы ввели некорректные символы! Вы можете ипользовать только буквы английского алфавита")
            if (response.get("code") == -1121):
                return ("Невозможно высичтать цену криптовалюты, нет привязки к USDT, либо данные были введены некорректно")
        else:
            return (f'Binance {crypto} \nПокупка: {response.get("price")}USDT')
    except Exception as ex:
        print(ex)
        return ("Произошла ошибка, поробуйте позже!")
