from django.core.management.base import BaseCommand, CommandError
from sys import platform
from telebot import types
from datetime import timedelta, datetime
from bot.userbot import user
import barcode
from barcode.writer import ImageWriter
import telebot
import logging
import traceback
import urllib

token = '1047483483:AAF6V0fMTNYRDjx0XZfHHGy3GdWiWmuporE'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def send_anytext(message):
    a = message.text
    codes = barcode.get_barcode_class('code39')
    ean = codes(str(a))
    now = datetime.now()
    times = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    fullname = ean.save(f'barcode/{times}_barcode')
    photo = open(fullname, 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()

class Command(BaseCommand):
    help = 'Команда запуска телеграм бота'

#    def add_arguments(self, parser):
#        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        bot.polling(none_stop=True)
