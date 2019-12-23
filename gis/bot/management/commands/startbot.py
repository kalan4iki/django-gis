from django.core.management.base import BaseCommand, CommandError
from bot.models import KNDhistor, DIPhistor, MKDhistor, Usersbot
from gis.settings import token, konfmain, DEBUG, logi
from bot.plot import plot
from sys import platform
from telebot import types
from datetime import timedelta, datetime
from bot.userbot import user
import telebot
import logging
import traceback
import urllib
import pandas as pd

if platform == 'linux' or platform == 'linux2':
    logging.basicConfig(filename=logi['linux']['direct']+logi['linux']['bot'], level=logging.INFO)
elif platform == 'win32':
    logging.basicConfig(filename=logi['win']['direct']+logi['win']['bot'], level=logging.INFO)
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    a = user(message)
    if a[0] == 'reg':
        bot.send_message(message.chat.id,'''Добро пожаловать. ✌
Бот для просмотра отчетов KND.
Вы были зарегистрированы в системе.
Вам доступен только отчет по территориям.
Чтобы получить больше доступа обратитесь к @vad_kalinin''', reply_markup=keyboard('0'))
    elif a[0] == 'exist':
        bot.send_message(message.chat.id,'''Вы уже зарегистрированы.
По всем вопросам писать @vad_kalinin''', reply_markup=keyboard('0'))

@bot.message_handler(content_types=["text"])
def send_anytext(message):
    # Блок запроса информации о пользователи
    print(message)
    ousers = user(message)[1]

    # Блок запроса времени и даты
    now = datetime.now()
    times = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    if now.day < 10:
        tinow = "0" + str(now.day) + "." + str(now.month) + "." + str(now.year)
    else:
        tinow = str(now.day) + "." + str(now.month) + "." + str(now.year)

    # Блок разбора сообщений
    if message.text == "Отчеты.":
        if int(ousers[0]) > 0:
            bot.send_message(message.chat.id, 'Выбирете отчеты по тематикам.', reply_markup=keyboard('1'))
        else:
            bot.send_message(message.chat.id, 'Доступ в отчеты не открыт.', reply_markup=keyboard('0'))
    elif message.text == "Динамики.":
        if int(ousers[1]) > 0:
            bot.send_message(message.chat.id, 'Выбирете динамики по тематикам.', reply_markup=keyboard('2'))
        else:
            bot.send_message(message.chat.id, 'Доступ в динамики не открыт.', reply_markup=keyboard('0'))
    elif message.text == 'Администратирование.':
        if int(ousers[2]) > 0:
            text = 'Данный раздел в разработке.'
            bot.send_message(message.chat.id, text, reply_markup=keyboard('2'))
        else:
            bot.send_message(message.chat.id, 'Доступ в раздел не открыт.', reply_markup=keyboard('0'))
    elif message.text == "Назад на главную.":
        bot.send_message(message.chat.id, 'На главную.', reply_markup=keyboard('0'))
    elif message.text == '✉️ Дворы.' or message.text == '/otch':
        if int(ousers[0]) < 1:
            text = 'Нет доступа в данный раздел.'
            bot.send_message(message.chat.id, text)
            return False
        try:
            b = KNDhistor.objects.filter(date=tinow)
            #if config.debug == True: logging.debug(str(b))
            if len(b) != 0:
                a = b[0]
                #text = f'На текущий момент проведен осмотр {a.complete} дворов из {a.maxdvor}. А именно {a.proc}%.'
                text = f'''Отчет по осмотру территорий на {a.times.day}.{a.times.month}.{a.times.year} {a.times.hour + 3}:{a.times.minute}:
Всего задач: {a.allz}
Взято в работу: {a.vrabote} ({a.vraboteproc}%)
Доступно: {a.dost} ({a.dostproc}%)
Завершено: {a.complete} ({a.completeproc}%)
Работ не требуется: {a.netreb} ({a.netrebproc}%)'''
            else:
                text = 'На текущую дату ещё нет информации.'
            logging.info('BOT ' + times + " successfully")
            bot.send_message(message.chat.id, text)
        except:
            logging.error('BOT ' + times + " Error data: " + traceback.format_exc())
            bot.send_message(message.from_user.id, 'Была допущена ошибка при подготовке сообщения.')
    elif message.text == '✉️ ДИП.':
        if int(ousers[1]) < 1:
            text = 'Нет доступа в данный раздел.'
            bot.send_message(message.chat.id, text)
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
    elif message.text == '📊 Дворы.':
        try:
            names = plot('knd')
            photo = open(names, 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
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
    elif message.text.split(' ')[0] == '/adddip':
        a = message.text.split(' ')
        data = {'date': a[1], 'alldv': a[2], 'complete': a[3], 'proc': a[4]}
        #editdb('dip', data)
        text = f'Запись сохранена.'
        bot.send_message(message.chat.id, text)
    elif message.text == 'Общий отчёт.':
        temp3 = 'В разработке'
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
    elif a == '3':
        btn9 = types.KeyboardButton('Назад на главную.')
        markup.row(btn9)
    return markup


class Command(BaseCommand):
    help = 'Команда запуска телеграм бота'

#    def add_arguments(self, parser):
#        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        bot.polling(none_stop=True)
