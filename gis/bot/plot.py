#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4:
#Библиотека построения графиков
from datetime import timedelta, datetime
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
#from config import maxdvor, db, debug, maxdip
from gis.settings import maxdvor, maxdip, DEBUG, path_plot, maxmkd
from bot.models import KNDhistor, DIPhistor, MKDhistor, Usersbot
#from bd import readdb
import matplotlib.pyplot as plt
import numpy as np

def plot(table):
    x = np.arange(7)
    now = datetime.now()
    times = str(now.hour) + str(now.minute) + str(now.second)
    dates = []
    for i in range(0, 7):
        temp = timedelta(i)
        tim = now - temp
        dates.append(tim)
    xdate = [dates[i] for i in range(6, -1, -1)]
    xdates = []
    for i in range(0, 7):
        temp = xdate[i]
        if temp.day < 10:
            xdates.append("0" + str(temp.day) + "." + str(temp.month) + "." + str(temp.year))
        else:
            xdates.append(str(temp.day) + "." + str(temp.month) + "." + str(temp.year))
    counts = []
    proc = []
    if DEBUG == True:
        print('xdates plt')
        print(xdates)
    for i in xdates:
        if table == 'knd':
            a = KNDhistor.objects.filter(date = i)
        elif table == 'dip':
            a = DIPhistor.objects.filter(date = i)
        elif table == 'mkd':
            a = MKDhistor.objects.filter(date = i)
        if len(a) != 0:
            counts.append(int(a[0].complete))
            proc.append(str(a[0].proc) + '%')
        else:
            counts.append(0)
            proc.append('0%')
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = []
    for i in range(0, 7):
        if xdate[i].weekday() == 5 or xdate[i].weekday() == 6:
            colors.append('yellow')
        else:
            colors.append('grey')
    if DEBUG == True:
        print('counts plt')
        print(counts)
        print('x')
        print(x)
    grap = ax.bar(x, counts, color=colors)
    plt.xticks(x, xdates)
    ax.grid(which="major", linestyle="--", linewidth=0.5)
    if table == 'knd':
        ax.set_title("Динамика по осмотру дворов за 7 дней.", fontsize=16)
        ax.set_ylabel("Количество дворов", fontsize=14)
        ax.axhline(maxdvor, ls='--', color='r')
        ax.set_ylim(0, maxdvor + 80)
    elif table == 'dip':
        ax.set_title("Динамика по осмотру ДИП за 7 дней.", fontsize=16)
        ax.set_ylabel("Количество ДИП", fontsize=14)
        ax.axhline(maxdip, ls='--', color='r')
        ax.set_ylim(0, maxdip + 80)
    elif table == 'mkd':
        ax.set_title("Динамика по осмотру МКД за 7 дней.", fontsize=16)
        ax.set_ylabel("Количество МКД", fontsize=14)
        ax.axhline(maxmkd, ls='--', color='r')
        ax.set_ylim(0, maxmkd + 80)
    ax.set_xlabel("Дни", fontsize=14)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_major_locator(MultipleLocator(25))
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    ax.tick_params(which='major', length=10, width=2)
    def autolabel(rects):
        i = 0
        for rect in rects:
            height = rect.get_height()
            if height < 60:
                yqwe = 5
            else:
                yqwe = -50
            ax.annotate('{}'.format(str(height) + '/' + proc[i]),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, yqwe), #color='white', # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', rotation=90)
            i += 1
    autolabel(grap)
    names = f'{path_plot}/{table}+{times}.png'
    #names = 'plt/' + times +'.png'
    plt.savefig(names, format='png', dpi=100)
    plt.clf()
    return names

if __name__ == '__main__':
    plot()
