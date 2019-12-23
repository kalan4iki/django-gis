# -*- coding: utf-8 -*-
#Исполняемый файл работы парсера
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from xml.dom.minidom import parseString
from bs4 import BeautifulSoup
from sys import platform
from bot.models import KNDhistor, DIPhistor, MKDhistor, Usersbot
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
    opts.add_argument('headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    if platform == 'linux' or platform == 'linux2':
        driver = webdriver.Chrome('/home/chromedriver',options=opts)
    elif platform == 'win32':
        driver = webdriver.Chrome(options=opts)
    driver.get("https://knd.mosreg.ru/snowfalls")
    time.sleep(5)
    driver.find_element_by_id('userName').clear()
    driver.find_element_by_id('userName').send_keys('tura241@yandex.ru')
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys('kn4325')
    driver.find_element_by_xpath('/html/body/div/form/div[3]/div/div/span/button').click()
    time.sleep(10)
    a = driver.page_source
    soup = BeautifulSoup(a, 'lxml')
    div = soup.find_all('div', class_ = 'ant-col ant-col-14')
    driver.quit()
    print(div)
    '''
    curr = {}
    table = []
    for i in tr:
        temp = i.find_all('td')
        #date = str(temp[2].text)
        temp3 = {}
        tempdate = temp[2].text.split('-')
        temp3['date'] = tempdate[0] + '.' + tempdate[1] + '.' + tempdate[2]
        temp3['alldv'] = temp[3].text
        temp3['complete'] = temp[4].text
        temp3['proc'] = temp[5].text
        table.append(temp3)
        if temp3['date'] == tinow:
            #print(temp3)
            curr = temp3
    if len(curr) == 0:
        curr['date'] = tinow
        curr['alldv'] = 0
        curr['complete'] = 0
        curr['proc'] = 0
    if typ == 'reg':
        editdb('knd', curr)
        logging.info(times + " parsing successfully." + f" date = {curr['date']}, dvor = {curr['complete']}, proc = {curr['proc']}")
    elif typ == 'new':
        #createdb('knd')
        writedb('knd', table)
        logging.info(times + " parsing successfully")
    '''
if __name__ == '__main__':
    parser()
