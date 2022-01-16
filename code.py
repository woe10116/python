
import telebot
import os
import requests
#from PIL import ImageGrab
import shutil
import sqlite3
import win32crypt
import subprocess
import platform
import webbrowser
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# from requests import getс

TOKEN = '1634916668:AAGcLMM0vvMcKn5E1RM-p6jG0TsjmS6h99A'
OWM_KEY = 'd5b90416aa002bfbff15f4ea6a72f717'

config_dict = get_default_config()
config_dict['language'] = 'ru'

bot = telebot.TeleBot(TOKEN)






def get_weather(location):
    try:
        owm = OWM(OWM_KEY, config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(location)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]

        answer = answer = f"В городе {location} сейчас {w.detailed_status}\n"
        answer += " Температура сейчас в районе " + str(temp) + "\n\n"

        if temp < -5:
            answer += "Сейчас ОЧЕНЬ ХОЛОДНО!"
            # img += Image.open(r'E:\2 cours\python\winter.jpg')
        elif temp < 5:
            answer += "Сейчас холодно, одевайся!"
            # img += Image.open(r'E:\2 cours\python\rain.jpg')
        elif temp < 15:
            answer += "Температура средняя,оденься потеплее!"
            # img += Image.open(r'E:\2 cours\python\medium.jpg')
        else:
            answer += "Температура нормальная, одевайcя как хочешь!"
            # img += Image.open(r'E:\2 cours\python\hot.jpg')
    except Exception as e:
        print('Error:', e)
        answer =  'Ошибка какая-то'

    return answer



def do_something_erronous():
    1 / 0


@bot.message_handler(content_types=['text'])
def send_echo(message):
    # логику работы с OWM переносим в отдельную функцию

    # запрашиваем текст о погоде в указанном городе
    answer = get_weather(message.text)

    bot.send_message(message.chat.id, answer, )
    # bot.send_photo(message.chat.id, get("https://i.ytimg.com/vi/EiZIa_htmpA/maxresdefault.jpg").content)
    # bot.send_photo(message.chat.id, img)



try:
    do_something_erronous()
except Exception as e:
    print('Error:', e)

bot.polling(none_stop=True)
