from django.core.management.base import BaseCommand, CommandError
from bot.models import KNDhistor, DIPhistor, MKDhistor, Usersbot
from gis.settings import token, konfmain, DEBUG
from bot.plot import plot
import telebot
import logging
import traceback
import urllib
import pandas as pd
from telebot import types
from datetime import timedelta, datetime

logging.basicConfig(filename="logs.log", level=logging.INFO)
bot = telebot.TeleBot(token)

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
            b = KNDhistor.objects.filter(date=tinow)
            #if config.debug == True: logging.debug(str(b))
            if len(b) != 0:
                a = b[0]
                #text = f'На текущий момент проведен осмотр {a.complete} дворов из {a.maxdvor}. А именно {a.proc}%.'
                text = f'На {a.times.hour + 3}:{a.times.minute} {a.times.day}.{a.times.month}.{a.times.year} проведен осмотр {a.complete} дворов из {a.maxdvor}. А именно {a.proc}%.'
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
            photo.close()
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '✉️ ДИП.':
        try:
            b = DIPhistor.objects.filter(date=tinow)
            #if config.debug == True: logging.debug(str(b))
            if len(b) != 0:
                a = b[0]
                #text =  f'На текущий момент проведен осмотр {a.complete} ДИП из {a.maxdvor}. А именно {a.proc}%.'
                text =  f'На {a.times.hour + 3}:{a.times.minute} {a.times.day}.{a.times.month}.{a.times.year} проведен осмотр {a.complete} ДИП из {a.maxdvor}. А именно {a.proc}%.'
            else:
                text = 'На текущую дату ещё нет информации.'
            logging.info('BOT ' + times + " successfully")
            bot.send_message(message.chat.id, text)
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '✉️ МКД.':
        try:
            b = MKDhistor.objects.filter(date=tinow)
            if len(b) != 0:
                a = b[0]
                #text =  f'На текущий момент проведен осмотр {a.complete} МКД из {a.maxdvor}. А именно {a.proc}%.'
                text =  f'На {a.times.hour + 3}:{a.times.minute} {a.times.day}.{a.times.month}.{a.times.year} проведен осмотр {a.complete} ДИП из {a.maxdvor}. А именно {a.proc}%.'
            else:
                text = 'На текущую дату ещё нет информации.'
            logging.info('BOT ' + times + " successfully")
            bot.send_message(message.chat.id, text)
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '📊 ДИП.':
        try:
            names = plot('dip')
            photo = open(names, 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '📊 МКД.':
        try:
            names = plot('mkd')
            photo = open(names, 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
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
        temp = [KNDhistor.objects.filter(date=tinow), DIPhistor.objects.filter(date=tinow), MKDhistor.objects.filter(date=tinow)]
        temp2 = [[], [], []]
        for i in temp:
            if len(i) != 0:
                j[0].append(str(i[0].maxdvor))
                j[1].append(str(i[0].complete))
                j[2].append(str(i[0].proc))
            else:
                j[0].append(str(0))
                j[1].append(str(0))
                j[2].append(str(0))
            temp2.append(j)
        print(temp2)
        temp3 = pd.DataFrame({'Всего': [j[0]],
                            'Выполнено': [j[1]],
                            'Процентов': [j[2]]
                            }, index = ['Дворы', 'ДИП', 'МКД'])
        bot.send_message(message.chat.id, temp3)

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


class Command(BaseCommand):
    help = 'Команда запуска телеграм бота'

#    def add_arguments(self, parser):
#        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        bot.polling(none_stop=True)
