import telebot
from telebot import types

from auth import token_bot
from mos_exchange import mos_exchange
from binance_rates import binance_rates
from tinkoff_exchange import tinkoff_exchange
from Binance_P2P_rates import binance_p2p_exchange

def start_bot(token_bot):
    bot = telebot.TeleBot(token_bot)
    #Вызываем фун-ю из библиотеки которая принимает в себя токен телеграм бота
    @bot.message_handler(commands=['start'])
    def say_hello(message):
        bot.send_message(message.chat.id,
                         "Привет! Я бот бот от студентов HSE, который может помочь тебе быстро отследить крус разной инсторанной валюты и криптовалюты")
        bot.send_message(message.chat.id,
                         "А также подскажу в каком банке сейчас выгоднее всего обменять валюту")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        binance_crypto_rates = types.KeyboardButton("Курс критптовалюты Binance")
        markup.add(binance_crypto_rates)
        binance_p2p = types.KeyboardButton("Курс на P2P Binance")
        markup.add(binance_p2p)
        tinkoff = types.KeyboardButton("Курс Тиньккофф")
        markup.add(tinkoff)
        mos = types.KeyboardButton("Курс МосБиржы")
        markup.add(mos)

    @bot.message_handler(content_types='text')
    def message_reply(message):
        if message.text == 'Курс критптовалюты Binance':
            bot.send_message(message.chat.id, "Напиши название криптовалюты в скоращенном формате, например: btc")
            @bot.message_handler(content_types=['text'])
            def new_value(new_value):
                try:
                    response = binance_rates(new_value)
                    if (response.get("code")):
                        if (response.get("code") == -1100):
                            bot.send_message(message.chat.id,
                                             "Вы ввели некорректные символы! Вы можете ипользовать только буквы английского алфавита")
                        if (response.get("code") == -1121):
                            bot.send_message(message.chat.id,
                                             "Невозможно высичтать цену криптовалюты, нет привязки к USDT, либо данные были введены некорректно")
                    else:
                        bot.send_message(message.chat.id, f'Binance {new_value.text.upper()} \nПокупка: {response.get("price")}USDT')

                except Exception as ex:
                    bot.send_message(message.chat.id,
                                     "Произошла ошибка, поробуйте позже!")
        elif message.text == "Курс на P2P Binance":
            bot.send_message(message.chat.id, "Напиши название криптовалюты например: usdt")
            @bot.message_handler(content_types=['text'])
            def new_value(new_value):
                try:
                    response = binance_p2p_exchange(new_value)
                    bot.send_message(message.chat.id, response)
                except Exception as ex:
                    bot.send_message(message.chat.id, ('Такой криптовалюты нет на Binance'))
        elif message.text == "Курс Тиньккофф":
            bot.send_message(message.chat.id, "Напиши название валюты в скоращенном формате, например: usd")
            @bot.message_handler(content_types=['text'])
            def new_value(new_value):
                try:
                    response = tinkoff_exchange(new_value)
                    bot.send_message(message.chat.id, response)
                except Exception as ex:
                    bot.send_message(message.chat.id, "Произошла ошибка, поробуйте позже!")
        elif message.text == 'Курс МосБиржы':
            bot.send_message(message.chat.id, "Напиши название валюты в скоращенном формате, например: usd")
            @bot.message_handler(content_types=['text'])
            def new_value(new_value):
                try:
                    response = mos_exchange(new_value)
                    bot.send_message(message.chat.id, response)
                except Exception as ex:
                    bot.send_message(message.chat.id,
                                     "Произошла ошибка, поробуйте позже!")

        else:
            bot.send_message(message.chat.id, "Я вас не понимаю")




    # @bot.message_handler(commands=['check_mos_rates'])
    # def check_bank(message):
    #     bot.send_message(message.chat.id, "Напиши название валюты в скоращенном формате, например: usd")
    #     @bot.message_handler(content_types=['text'])
    #     def new_value(new_value):
    #         try:
    #             response = mos_exchange(new_value)
    #             bot.send_message(message.chat.id, response)
    #         except Exception as ex:
    #             bot.send_message(message.chat.id,
    #                              "Произошла ошибка, поробуйте позже!")
    # @bot.message_handler(commands=['check_tinkoff_rates'])
    # def check_bank(message):
    #     bot.send_message(message.chat.id, "Напиши название валюты в скоращенном формате, например: usd")
    #     @bot.message_handler(content_types=['text'])
    #     def new_value(new_value):
    #         try:
    #             response = tinkoff_exchange(new_value)
    #             bot.send_message(message.chat.id, response)
    #         except Exception as ex:
    #             bot.send_message(message.chat.id, "Произошла ошибка, поробуйте позже!")




    bot.polling() #Используется для того чтобы бот оставлася активным и реагировал на сообщения



if __name__ == '__main__':
    start_bot(token_bot)