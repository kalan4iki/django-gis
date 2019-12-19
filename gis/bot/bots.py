# -*- coding: utf-8 -*-
#Исполняемый файл работы бота
import config
import telebot
import logging
import traceback
import urllib
from telebot import types
from datetime import timedelta, datetime
from plot import plot
from bot.models import KNDhistor, DIPhistor, Usersbot


logging.basicConfig(filename="logs.log", level=logging.INFO)
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(
		message.chat.id,
		'''Добро пожаловать. ✌
Бот для просмотра отчетов KND.
		''', reply_markup=keyboard('0'))

@bot.message_handler(content_types=["text"])
def send_anytext(message):
    now = datetime.now()
    times = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    if now.day < 10:
        tinow = "0" + str(now.day) + "." + str(now.month) + "." + str(now.year)
    else:
        tinow = str(now.day) + "." + str(now.month) + "." + str(now.year)
    if message.text == "Отчеты.":
        bot.send_message(message.chat.id, 'Выбирете отчеты по тематикам.', reply_markup=keyboard('1'))
    elif message.text == "Динамики.":
        bot.send_message(message.chat.id, 'Выбирете динамики по тематикам.', reply_markup=keyboard('2'))
    elif message.text == "Назад на главную.":
        bot.send_message(message.chat.id, 'На главную.', reply_markup=keyboard('0'))
    elif message.text == '✉️ Дворы.' or message.text == '/otch':
        try:
	        #b = readdb('knd', {'date': tinow})
            if config.debug == True: logging.debug(str(b))
            if len(b) != 0:
                #a = b[0]
                text = 'На текущий момент проведен осмотр ' + str(a[2]) + ' дворов из ' + str(a[1]) + '. А именно ' + str(a[3]) + '%.'
            else:
                text = 'На текущую дату ещё нет информации.'
            logging.info('BOT ' + times + " successfully")
            bot.send_message(message.chat.id, text)
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '📊 Дворы.':
        try:
            names = plot('knd')
            photo = open(names, 'rb')
            bot.send_photo(message.chat.id, photo)
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '✉️ ДИП.':
        try:
            b = readdb('dip', {'date': tinow})
            if config.debug == True: logging.debug(str(b))
            if len(b) != 0:
                a = b[0]
                text = 'На текущий момент проведен осмотр ' + str(a[2]) + ' ДИП из ' + str(a[1]) + '. А именно ' + str(a[3]) + '%.'
            else:
                text = 'На текущую дату ещё нет информации.'
            logging.info('BOT ' + times + " successfully")
            bot.send_message(message.chat.id, text)
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '✉️ МКД.':
        text = 'Данный раздел в разработке.'
        bot.send_message(message.chat.id, text)
    elif message.text == '📊 ДИП.':
        try:
            names = plot('dip')
            photo = open(names, 'rb')
            bot.send_photo(message.chat.id, photo)
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '📊 МКД.':
        text = 'Данный раздел в разработке.'
        bot.send_message(message.chat.id, text)
    elif message.text == 'Администратирование.':
        text = 'Данный раздел в разработке.'
        bot.send_message(message.chat.id, text)
    elif message.text.split(' ')[0] == '/adddip':
        a = message.text.split(' ')
        data = {'date': a[1], 'alldv': a[2], 'complete': a[3], 'proc': a[4]}
        #editdb('dip', data)
        text = f'Запись сохранена.'
        bot.send_message(message.chat.id, text)
    elif message.text == 'Общий отчёт.':
        text = 'Данный раздел в разработке.'
        bot.send_message(message.chat.id, text)

def keyboard(a):
    markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    if a == '0':
        btn1 = types.KeyboardButton('Отчеты.')
        btn2 = types.KeyboardButton('Динамики.')
        btn3 = types.KeyboardButton('Администратирование.')
        markup.add(btn1, btn2)
        markup.row(btn3)
    elif a == '1':
        btn1 = types.KeyboardButton('✉️ Дворы.')
        btn2 = types.KeyboardButton('✉️ ДИП.')
        btn3 = types.KeyboardButton('✉️ МКД.')
        btn4 = types.KeyboardButton('Общий отчёт.')
        btn5 = types.KeyboardButton('Назад на главную.')
        markup.row(btn1, btn2, btn3)
        markup.row(btn4)
        markup.row(btn5)
    elif a == '2':
        btn1 = types.KeyboardButton('📊 Дворы.')
        btn2 = types.KeyboardButton('📊 ДИП.')
        btn3 = types.KeyboardButton('📊 МКД.')
        btn4 = types.KeyboardButton('Назад на главную.')
        markup.row(btn1, btn2, btn3)
        markup.row(btn4)
    return markup

if __name__ == '__main__':
    now = datetime.now
    bot.polling(none_stop=True)
