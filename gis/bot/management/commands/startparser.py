# -*- coding: utf-8 -*-
#Исполняемый файл работы парсера
from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from xml.dom.minidom import parseString
from bs4 import BeautifulSoup
from sys import platform
from bot.models import KNDhistor, DIPhistor, MKDhistor, Usersbot
from gis.settings import DEBUG, username_knd, password_knd, path_driver
import lxml
import time
import datetime
import logging
import argparse
import traceback

parser = argparse.ArgumentParser(description='Print an argument several times')
logging.basicConfig(filename="logs.log", level=logging.INFO)

def parser():
    now = datetime.datetime.now()
    times = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    if now.day < 10:
        tinow = "0" + str(now.day) + "." + str(now.month) + "." + str(now.year)
    else:
        tinow = str(now.day) + "." + str(now.month) + "." + str(now.year)
    opts = Options()
    #opts.add_argument('headless')
    #opts.add_argument('--no-sandbox')
    #opts.add_argument('--disable-dev-shm-usage')
    if platform == 'linux' or platform == 'linux2':
        driver = webdriver.Chrome(path_driver['linux'],options=opts)
    elif platform == 'win32':
        driver = webdriver.Chrome(path_driver['win'], options=opts)
    driver.get("https://knd.mosreg.ru/snowfalls")
    time.sleep(5)
    driver.find_element_by_id('userName').clear()
    driver.find_element_by_id('userName').send_keys(username_knd)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(password_knd)
    driver.find_element_by_xpath('/html/body/div/form/div[3]/div/div/span/button').click()
    time.sleep(10)
    a = driver.page_source
    soup = BeautifulSoup(a, 'lxml')
    div = soup.find_all('div', class_ = 'ant-col ant-col-14')
    driver.quit()
    temp = []
    proc = []
    for i in div:
        a = i.text.split('%')
        temp.append(a[1].split(' ')[-1].split(')')[0])
        proc.append(a[0])
    tisplit = tinow.split('.')
    a = KNDhistor(date = tinow, day=tisplit[0], month=tisplit[1], year=tisplit[2],
                    vrabote= int(temp[0]), dost= int(temp[1]), complete= int(temp[2]), netreb= int(temp[3]),
                    vraboteproc= float(proc[0]), dostproc= float(proc[1]), completeproc= float(proc[2]), netrebproc= float(proc[3]))
    a.save()

if __name__ == '__main__':
    parser()

class Command(BaseCommand):
    help = 'Команда запуска телеграм бота'

#    def add_arguments(self, parser):
#        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        parser()