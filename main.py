import requests
import telebot
from telebot import types
from auth import token_bot
from mos_exchange import mos_exchange
from binance_rates import binance_rates
from tinkoff_exchange import tinkoff_exchange
from Binance_P2P_rates import binance_p2p_exchange
from cb_exchange import cb_exchange


def start_bot(token_bot):
    bot = telebot.TeleBot(token_bot)
    # Вызываем фун-ю из библиотеки которая принимает в себя токен телеграм бота

    @bot.message_handler(commands=['start'])
    def start_command(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Курс критптовалюты Binance"),
                   types.KeyboardButton("Курс на P2P Binance"), types.KeyboardButton("Курс МосБиржи"),types.KeyboardButton("Курс Тинькофф"), types.KeyboardButton("Курс ЦБ РФ"))
        msg = bot.send_message(message.chat.id,
                               "Привет! Я бот бот от студентов HSE, который может помочь тебе быстро отследить крус разной инсторанной валюты и криптовалюты",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, user_answer)

    @bot.message_handler(func=lambda message: message.text == "Назад")
    def back(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Курс критптовалюты Binance"),
                   types.KeyboardButton("Курс на P2P Binance"), types.KeyboardButton("Курс МосБиржи"), types.KeyboardButton("Курс Тинькофф"), types.KeyboardButton("Курс ЦБ РФ"))
        msg = bot.send_message(message.chat.id, "Выбери действие",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, user_answer)



    def user_answer(message):
        if message.text == "Курс критптовалюты Binance":
            msg = bot.send_message(message.chat.id, "Введите крипту")
            bot.register_next_step_handler(msg, get_crypto_rate)
        elif message.text == "Курс на P2P Binance":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("USDT"), types.KeyboardButton("BUSD"), types.KeyboardButton("BNB"), types.KeyboardButton(
                "ETH"), types.KeyboardButton("BTC"), types.KeyboardButton("RUB"), types.KeyboardButton("SHIB"))
            msg = bot.send_message(
                message.chat.id, "Введите крипту", reply_markup=markup)
            bot.register_next_step_handler(msg, get_p2p_rate)
        elif message.text == "Курс МосБиржи":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("USD"), types.KeyboardButton("CNY"), types.KeyboardButton("EUR"), types.KeyboardButton(
                "BYN"), types.KeyboardButton("TRY"))
            msg = bot.send_message(
                message.chat.id, "Введите крипту", reply_markup=markup)
            bot.register_next_step_handler(msg, get_mos_ex)
        elif message.text == "Курс Тинькофф":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            arr_rates = requests.get('https://acdn.tinkoff.ru/mp-resources/currencies_weights.json')
            res = arr_rates.json()
            for i in res:
                markup.add(types.KeyboardButton(i))
            msg = bot.send_message(
                message.chat.id, "Введите валюту", reply_markup=markup)
            bot.register_next_step_handler(msg, get_tinkoff)
        elif message.text == "Курс ЦБ РФ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            arr_rates = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']
            for i in arr_rates:
                markup.add(types.KeyboardButton(i))
            msg = bot.send_message(
                message.chat.id, "Введите валюту", reply_markup=markup)
            bot.register_next_step_handler(msg, get_cb)


    def get_crypto_rate(message):
        response = binance_rates(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, response, reply_markup=markup)

    def get_p2p_rate(message):
        response = binance_p2p_exchange(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, response, reply_markup=markup)

    def get_mos_ex(message):
        response = mos_exchange(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, response, reply_markup=markup)


    def get_tinkoff(message):
        response = tinkoff_exchange(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, response, reply_markup=markup)


    def get_cb(message):
        response = cb_exchange(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, response, reply_markup=markup)


    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.polling()  # Используется для того чтобы бот оставлася активным и реагировал на сообщения


if __name__ == '__main__':
    start_bot(token_bot)
