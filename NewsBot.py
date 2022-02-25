import telebot
import requests
from bs4 import BeautifulSoup as BS
from config import *
from db import *
from telebot import types
from schedule import every, run_pending
import time
from threading import Thread
import random
from fake_useragent import UserAgent

bot = telebot.TeleBot(token)
BotDB = BotDB()
btns = list(links.keys())


def get_currency():
    r = requests.get("https://invest.yandex.ru/catalog/currency/usd/")
    html = BS(r.content, "html.parser")
    dolVal = html.find_all(class_="QV5TZ0Aew_2aahfCgGmv")[0].text
    dolProc = html.find_all(class_="rzv7e6OPChq71rCQBr9H _9RS0xgK34zINnxUjOgH")[0].text.split("  ₽")

    r = requests.get("https://invest.yandex.ru/catalog/currency/eur/")
    html = BS(r.content, "html.parser")
    euVal = html.find_all(class_="QV5TZ0Aew_2aahfCgGmv")[0].text
    euProc = html.find_all(class_="rzv7e6OPChq71rCQBr9H _9RS0xgK34zINnxUjOgH")[0].text.split("  ₽")

    return ((dolVal, dolProc), (euVal, euProc))


# print("−" in get_currency()[0][1][0])

def get_horoscope(znak):
    r = requests.get(links[znak])
    html = BS(r.content, "html.parser")

    soup1 = html.select('h1')[0].text
    soup = html.select('p')
    return soup1, soup


def get_news(url):
    r = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    html = BS(r.content, "html.parser")
    news = html.find_all(class_="mg-card__title")
    return news


def send_news(chat_id, topic, article):
    markup = types.InlineKeyboardMarkup()
    skip = types.InlineKeyboardButton(text='Не интересно', callback_data="skip")
    det = types.InlineKeyboardButton(text='Подробнее', url=topic)
    markup.add(skip, det)
    markup.add(types.KeyboardButton(text="Меню↩"))
    if article < len(get_news(topic)) - 1:
        bot.send_message(chat_id, get_news(topic)[article].text, reply_markup=markup)
        BotDB.update_article(chat_id, article + 1)
        BotDB.update_topic(chat_id, topic)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton(text="Меню↩"))
        bot.send_message(chat_id, "Новости на эту тему закончились", reply_markup=markup)


def send_hor():
    for i in BotDB.get_id():
        if BotDB.get_znak(i[0]) in btns:
            bot.send_message(i[0], get_horoscope(BotDB.get_znak(i[0]))[0])
            for j in get_horoscope(BotDB.get_znak(i[0]))[1]:
                bot.send_message(i[0], j)


every().day.at("08:00").do(send_hor)


def work():
    while True:
        run_pending()
        time.sleep(1)


th = Thread(target=work)
th.start()


# while True:
#   run_pending()
#  time.sleep(1)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id,
                     "{0.first_name}, здравствуйте, я новостной бот. Напишите мне день и месяц вашего рождения (через точку), чтобы получать гороскоп".format(
                         message.from_user))
    if not BotDB.user_exists(message.chat.id):
        BotDB.add_user(message.chat.id, "welcome", "{0.first_name}".format(message.from_user),
                       message.from_user.username, "pass")
    else:
        BotDB.update_status(message.chat.id, "welcome")


@bot.message_handler(commands=["активировать"])
def activate(message):
    bot.send_message(message.chat.id,
                     "{0.first_name}, напишите мне день и месяц вашего рождения (через точку), чтобы получать гороскоп".format(
                         message.from_user))
    if not BotDB.user_exists(message.chat.id):
        BotDB.add_user(message.chat.id, "welcome", "{0.first_name}".format(message.from_user),
                       message.from_user.username, "pass")
    else:
        BotDB.update_status(message.chat.id, "welcome")


@bot.message_handler(commands=["отказаться"])
def cancel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton(text="Меню↩")
    markup.add(back)
    BotDB.update_znak(message.chat.id, "pass")
    bot.send_message(message.chat.id, "Рассылка отменена")
    bot.send_message(message.chat.id,
                     "У вас не подключена рассылка, чтобы её активировать введите команду '/активировать'",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "skip":
        send_news(call.message.chat.id, BotDB.get_topic(call.message.chat.id), BotDB.get_article(call.message.chat.id))
    else:
        BotDB.update_status(call.message.chat.id, "pass")
        bot.delete_message(call.message.chat.id, call.message.message_id)
        BotDB.update_article(call.message.chat.id, 0)
        send_news(call.message.chat.id, call.data, 0)


@bot.message_handler(content_types=["text"])
def chat(message):
    if message.text == "Меню↩":
        BotDB.update_status(message.chat.id, "menu")
    if message.text == "Гороскопы🪐":
        BotDB.update_status(message.chat.id, "horoscope")
    if message.text == "Новости📰":
        BotDB.update_status(message.chat.id, "news")
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
                znak = btns[0]

            elif (data[0] >= 20 and data[0] <= 30 and data[1] == 4) or (
                    data[1] == 5 and data[0] >= 1 and data[0] <= 20):

                znak = btns[1]

            elif (data[0] >= 21 and data[0] <= 31 and data[1] == 5) or (
                    data[1] == 6 and data[0] >= 1 and data[0] <= 21):

                znak = btns[2]

            elif (data[0] >= 22 and data[0] <= 30 and data[1] == 6) or (
                    data[1] == 7 and data[0] >= 1 and data[0] <= 22):

                znak = btns[3]

            elif (data[0] >= 23 and data[0] <= 31 and data[1] == 7) or (
                    data[1] == 8 and data[0] >= 1 and data[0] <= 22):

                znak = btns[4]

            elif (data[0] >= 23 and data[0] <= 31 and data[1] == 8) or (
                    data[1] == 9 and data[0] >= 1 and data[0] <= 22):

                znak = btns[5]

            elif (data[0] >= 23 and data[0] <= 30 and data[1] == 9) or (
                    data[1] == 10 and data[0] >= 1 and data[0] <= 23):

                znak = btns[6]

            elif (24 <= data[0] <= 31 and data[1] == 10) or (
                    data[1] == 11 and 1 <= data[0] <= 22):

                znak = btns[7]

            elif (23 <= data[0] <= 30 and data[1] == 11) or (
                    data[1] == 12 and 1 <= data[0] <= 21):

                znak = btns[8]

            elif (22 <= data[0] <= 31 and data[1] == 12) or (
                    data[1] == 1 and 1 <= data[0] <= 20):

                znak = btns[9]

            elif (21 <= data[0] <= 31 and data[1] == 1) or (
                    data[1] == 2 and 1 <= data[0] <= 18):

                znak = btns[10]

            elif (19 <= data[0] <= 29 and data[1] == 2) or (
                    data[1] == 3 and 1 <= data[0] <= 20):

                znak = btns[11]

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text="Меню↩")
            markup.add(btn1)
            bot.send_message(message.chat.id, f"А вы знали, что Вы {znak}?")
            BotDB.update_status(message.chat.id, "pass")
            BotDB.update_znak(message.chat.id, znak)
            bot.send_message(message.chat.id, "Теперь каждое утро в 9 часов вы будете получать актуальный гороскоп,"
                                              " чтобы отменить рассылку введите команду '/отказаться'",
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Введены невенрные данные, попробуйте еще раз")

    if BotDB.get_status(message.chat.id) == "news":
        markup = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='Казань🕌', callback_data="https://yandex.ru/news/region/kazan")
        btn_2 = types.InlineKeyboardButton(text='Коронавирус🦠',
                                           callback_data="https://yandex.ru/news/rubric/koronavirus")
        btn_3 = types.InlineKeyboardButton(text='Политика🇺🇳', callback_data="https://yandex.ru/news/rubric/politics")
        btn_4 = types.InlineKeyboardButton(text='Экономика📈', callback_data="https://yandex.ru/news/rubric/business")
        btn_5 = types.InlineKeyboardButton(text='Спорт⚽️',
                                           callback_data="https://yandex.ru/sport?utm_source=yxnews&utm_medium=desktop")
        btn_6 = types.InlineKeyboardButton(text='Происшествия🚨',
                                           callback_data="https://yandex.ru/news/rubric/incident")
        btn_7 = types.InlineKeyboardButton(text='Культура🎨', callback_data="https://yandex.ru/news/rubric/culture")
        btn_8 = types.InlineKeyboardButton(text='Технологии💻', callback_data="https://yandex.ru/news/rubric/computers")
        markup.add(btn_1)
        markup.add(btn_2)
        markup.add(btn_3)
        markup.add(btn_4)
        markup.add(btn_5)
        markup.add(btn_6)
        markup.add(btn_7)
        markup.add(btn_8)
        bot.send_message(message.chat.id, "Выберите тему", reply_markup=markup)

    if BotDB.get_status(message.chat.id) == "menu":
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn1 = types.KeyboardButton(text="Гороскопы🪐")
        btn2 = types.KeyboardButton(text="Курсы валют💰")
        btn3 = types.KeyboardButton(text="Новости📰")
        markup.add(btn1, btn2, btn3)
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
        back = types.KeyboardButton(text="Меню↩")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, back)
        bot.send_message(message.chat.id, "Выберите знак зодиака для которого хотите узнать гороскоп",
                         reply_markup=markup)

    if BotDB.get_status(message.chat.id) == "curr":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text="Меню↩")
        markup.add(back)
        znach = get_currency()
        if "−" in znach[0][1][0]:
            dol = f"Доллар💵: {znach[0][0]}, за день: {znach[0][1][1]}🔻"
        else:
            dol = f"Доллар💵: {znach[0][0]}, за день: {znach[0][1][1]}🔺"

        if "−" in znach[1][1][0]:
            eu = f"Евро💶: {znach[1][0]}, за день: {znach[1][1][1]}🔻"
        else:
            eu = f"Евро💶: {znach[1][0]}, за день: {znach[1][1][1]}🔺"

        bot.send_message(message.chat.id, f"""{dol}

{eu}""", reply_markup=markup)
        BotDB.update_status(message.chat.id, "pass")


if __name__ == '__main__':
    bot.infinity_polling()
