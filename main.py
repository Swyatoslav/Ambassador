import os
import time

import requests
from helper import Helper
import telebot
from telebot.types import ReplyKeyboardRemove


# Preparation
root = os.path.dirname(os.path.abspath(__file__))
helper = Helper()
token = helper.get_bot_token(root)
bot = telebot.TeleBot(token, threaded=False)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    pass


@bot.message_handler(commands=['start', ])
def start_message(message):
    try:
        if message.text.lower() == '/start':
            helper.send_message(bot, message.chat.id, 'Start message', reply_markup=ReplyKeyboardRemove())
    except Exception as err:
        pass


@bot.message_handler()
def send_text(message):
    try:
        pass
    except Exception as err:
        pass


# Команда для запуска бота

if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=120)
        except requests.exceptions.ConnectTimeout:
            bot.stop_polling()
            print('Timeout')
            time.sleep(1)
            bot.polling(none_stop=True, interval=1, timeout=120)
