import telebot
import requests
from bs4 import BeautifulSoup as BS
from config import *
from db import *
from telebot import types
import datetime as dt

bot = telebot.TeleBot(token)
BotDB = BotDB()
btns = list(links.keys())


def get_horoscope(znak):
    r = requests.get(links[znak])
    html = BS(r.content, "html.parser")

    soup1 = html.select('h1')[0].text
    soup = html.select('p')
    return soup1, soup


def get_currency():
    r = requests.get("https://invest.yandex.ru/catalog/currency/")
    html = BS(r.content, "html.parser")
    a = html.find_all(class_="JGT__mSaFfXxcOb2oGto")
    b = html.find_all(class_="FKk_VD_UBO4sS_Tt6IHI")
    return [(a[0], b[0]), (a[1], b[1])]


if dt.datetime.now().hour == 9:
    for i in BotDB.get_id():
        bot.send_message(i[0], get_horoscope(BotDB.get_znak(i[0]))[0])
        for j in get_horoscope(BotDB.get_znak(i[0]))[1]:
            bot.send_message(i[0], j)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id,
                     "{0.first_name}, здравствуй, я новостной бот. Напишите мне день и месяц вашего рождения (через точку), чтобы получать гороскоп".format(
                         message.from_user))
    if not BotDB.user_exists(message.chat.id):
        BotDB.add_user(message.chat.id, "welcome", "{0.first_name}".format(message.from_user),
                       message.from_user.username, "pass")
    else:
        BotDB.update_status(message.chat.id, "welcome")


@bot.message_handler(content_types=["text"])
def chat(message):
    if message.text == "Меню↩":
        BotDB.update_status(message.chat.id, "menu")
    if message.text == "Гороскопы🪐":
        BotDB.update_status(message.chat.id, "horoscope")
    if message.text == "Курсы валют💰":
        BotDB.update_status(message.chat.id, "curr")
    if message.text in btns:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text="Меню↩")
        markup.add(back)
        bot.send_message(message.chat.id, get_horoscope(message.text)[0])
        for i in get_horoscope(message.text)[1]:
            bot.send_message(message.chat.id, i.text, reply_markup=markup)
        BotDB.update_status(message.chat.id, "pass")

    if BotDB.get_status(message.chat.id) == "welcome":
        data = list(map(int, message.text.split(".")))
        if len(data) == 2 and 0 < data[0] < 32 and 0 < data[1] < 13:
            znak = "Овен"
            if (21 <= data[0] <= 31 and data[1] == 3) or (data[1] == 4 and 1 <= data[0] <= 19):
                znak = "Овен"

            elif (data[0] >= 20 and data[0] <= 30 and data[1] == 4) or (
                    data[1] == 5 and data[0] >= 1 and data[0] <= 20):

                znak = "Телец"

            elif (data[0] >= 21 and data[0] <= 31 and data[1] == 5) or (
                    data[1] == 6 and data[0] >= 1 and data[0] <= 21):

                znak = "Близнецы"

            elif (data[0] >= 22 and data[0] <= 30 and data[1] == 6) or (
                    data[1] == 7 and data[0] >= 1 and data[0] <= 22):

                znak = "Рак"

            elif (data[0] >= 23 and data[0] <= 31 and data[1] == 7) or (
                    data[1] == 8 and data[0] >= 1 and data[0] <= 22):

                znak = "Лев"

            elif (data[0] >= 23 and data[0] <= 31 and data[1] == 8) or (
                    data[1] == 9 and data[0] >= 1 and data[0] <= 22):

                znak = "Дева"

            elif (data[0] >= 23 and data[0] <= 30 and data[1] == 9) or (
                    data[1] == 10 and data[0] >= 1 and data[0] <= 23):

                znak = "Весы"

            elif (24 <= data[0] <= 31 and data[1] == 10) or (
                    data[1] == 11 and 1 <= data[0] <= 22):

                znak = "Скорпион"

            elif (23 <= data[0] <= 30 and data[1] == 11) or (
                    data[1] == 12 and 1 <= data[0] <= 21):

                znak = "Стрелец"

            elif (22 <= data[0] <= 31 and data[1] == 12) or (
                    data[1] == 1 and 1 <= data[0] <= 20):

                znak = "Козерог"

            elif (21 <= data[0] <= 31 and data[1] == 1) or (
                    data[1] == 2 and 1 <= data[0] <= 18):

                znak = "Водолей"

            elif (19 <= data[0] <= 29 and data[1] == 2) or (
                    data[1] == 3 and 1 <= data[0] <= 20):

                znak = "Рыбы"

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text="Меню↩")
            markup.add(btn1)
            bot.send_message(message.chat.id, f"А вы знали, что вы {znak}")
            BotDB.update_status(message.chat.id, "pass")
            BotDB.update_znak(message.chat.id, znak)
            bot.send_message(message.chat.id, "Теперь каждое утро в 9 часов вы будете получать актуальный гороскоп",
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Введены невенрные данные, попробуйте еще раз")

    if BotDB.get_status(message.chat.id) == "menu":
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn1 = types.KeyboardButton(text="Гороскопы🪐")
        btn2 = types.KeyboardButton(text="Курсы валют💰")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы в меню", reply_markup=markup)

    if BotDB.get_status(message.chat.id) == "horoscope":
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn1 = types.KeyboardButton(text=btns[0])
        btn2 = types.KeyboardButton(text=btns[1])
        btn3 = types.KeyboardButton(text=btns[2])
        btn4 = types.KeyboardButton(text=btns[3])
        btn5 = types.KeyboardButton(text=btns[4])
        btn6 = types.KeyboardButton(text=btns[5])
        btn7 = types.KeyboardButton(text=btns[6])
        btn8 = types.KeyboardButton(text=btns[7])
        btn9 = types.KeyboardButton(text=btns[8])
        btn10 = types.KeyboardButton(text=btns[9])
        btn11 = types.KeyboardButton(text=btns[10])
        btn12 = types.KeyboardButton(text=btns[11])
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
        bot.send_message(message.chat.id, "Выберите знак задиака для которого хотите узнать гороскоп",
                         reply_markup=markup)

    if BotDB.get_status(message.chat.id) == "curr":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text="Меню↩")
        markup.add(back)
        bot.send_message(message.chat.id,
                         f"""Доллар💵: {get_currency()[0][0].text}, за день: {get_currency()[0][1].text}
                         Евро💶: {get_currency()[1][0].text}, за день: {get_currency()[1][1].text}""",
                         reply_markup=markup)
        BotDB.update_status(message.chat.id, "pass")


if __name__ == '__main__':
    bot.infinity_polling()
