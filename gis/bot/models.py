from django.db import models
import uuid

class KNDhistor(models.Model): #Отчеты по территориям
    date = models.CharField(max_length=20, help_text='Дата отчета.',
                            verbose_name = 'Дата', primary_key = True)
    day = models.IntegerField(help_text='День.', verbose_name = 'День', blank=True)
    month = models.IntegerField(help_text='Месяц.', verbose_name = 'Месяц', blank=True)
    year = models.IntegerField(help_text='Год.', verbose_name = 'Год', blank=True)
    allz = models.IntegerField(help_text='Всего задач.', verbose_name = 'Всего задач')
    vrabote = models.IntegerField(help_text='В работе.',
                            verbose_name = 'В работе')
    dost = models.IntegerField(help_text='Доступно.',
                            verbose_name = 'Доступно')
    complete = models.IntegerField(help_text='Выполнено.',
                            verbose_name = 'Выполнено')
    netreb = models.IntegerField(help_text='Не ребуются.',
                            verbose_name = 'Не ребуются')
    vraboteproc = models.FloatField(help_text='В работе процентов.',
                            verbose_name = 'В работе процентов')
    dostproc = models.FloatField(help_text='Доступно процентов.',
                            verbose_name = 'Доступно процентов')
    completeproc = models.FloatField(help_text='Выполнено процентов.',
                            verbose_name = 'Выполнено процентов')
    netrebproc = models.FloatField(help_text='Не ребуются процентов.',
                            verbose_name = 'Не ребуются процентов')
    times = models.DateTimeField(auto_now= True, help_text='Время отчета.',
                            verbose_name = 'Время проверки')

    class Meta:
        ordering = ['year', 'month', 'day']
        verbose_name = 'отчет по осмотру территорий'
        verbose_name_plural = 'отчеты по осмотру территорий'

    def __str__(self):
        return self.date

class DIPhistor(models.Model): #Отчеты по ДИП
    date = models.CharField(max_length=20, help_text='Дата отчета.',
                            verbose_name = 'Дата', primary_key = True)
    day = models.IntegerField(help_text='День.', verbose_name = 'День', blank=True)
    month = models.IntegerField(help_text='Месяц.', verbose_name = 'Месяц', blank=True)
    year = models.IntegerField(help_text='Год.', verbose_name = 'Год', blank=True)
    maxdvor = models.IntegerField(help_text='Всего ДИП.',
                            verbose_name = 'Всего ДИП')
    complete = models.IntegerField(help_text='Выполнено осмотров.',
                            verbose_name = 'Выполнено осмотров')
    proc = models.IntegerField(help_text='Процент выполнения.',
                            verbose_name = 'Процент выполнения')
    times = models.DateTimeField(auto_now= True, help_text='Время отчета.',
                            verbose_name = 'Время')

    class Meta:
        ordering = ['year', 'month', 'day']
        verbose_name = 'отчет по осмотру ДИП'
        verbose_name_plural = 'отчеты по осмотру ДИП'

    def __str__(self):
        return self.date

class MKDhistor(models.Model): #Отчеты по ДИП
    date = models.CharField(max_length=20, help_text='Дата отчета.',
                            verbose_name = 'Дата', primary_key = True)
    day = models.IntegerField(help_text='День.', verbose_name = 'День', blank=True)
    month = models.IntegerField(help_text='Месяц.', verbose_name = 'Месяц', blank=True)
    year = models.IntegerField(help_text='Год.', verbose_name = 'Год', blank=True)
    maxdvor = models.IntegerField(help_text='Всего МКД.',
                            verbose_name = 'Всего МКД')
    complete = models.IntegerField(help_text='Выполнено осмотров.',
                            verbose_name = 'Выполнено осмотров')
    proc = models.IntegerField(help_text='Процент выполнения.',
                            verbose_name = 'Процент выполнения')
    times = models.DateTimeField(auto_now= True, help_text='Время отчета.',
                            verbose_name = 'Время')

    class Meta:
        ordering = ['year', 'month', 'day']
        verbose_name = 'отчет по осмотру МКД'
        verbose_name_plural = 'отчеты по осмотру МКД'

    def __str__(self):
        return self.date

class Usersbot(models.Model):
    username = models.CharField(max_length=20, help_text='username',
                            verbose_name = 'username')
    id = models.IntegerField(help_text='ID пользователя.', verbose_name = 'ID',
                            primary_key = True)
    email = models.EmailField(max_length=40, help_text='Почта',
                            verbose_name = 'Почта пользователя', blank = True)
    last_name = models.CharField(max_length=20, help_text='Фамилия',
                            verbose_name = 'Фамилия', blank = True)
    first_name = models.CharField(max_length=20, help_text='Имя',
                            verbose_name = 'Имя', blank = True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, help_text='Статус регистрации',
                            verbose_name = 'Статус', default = '0')
    role = models.CharField(max_length=20, help_text='Роль пользователя',
                            verbose_name = 'Роль', default = '244')

    class Meta:
        ordering = ['username']
        verbose_name = 'пользователь бота'
        verbose_name_plural = 'пользователи бота'

    def __str__(self):
        return self.username

class Konfbot(models.Model):
    id = models.IntegerField(help_text='ID конференции.', verbose_name = 'ID',
                            primary_key = True)
    name = models.CharField(max_length=20, help_text='Название конференции',
                            verbose_name = 'Название конференции')
    status = models.CharField(max_length=20, help_text='Статус регистрации',
                            verbose_name = 'Статус', default = '0')
    role = models.CharField(max_length=20, help_text='Роль пользователя',
                            verbose_name = 'Роль', default = '444')

    class Meta:
        ordering = ['id']
        verbose_name = 'пользователь бота'
        verbose_name_plural = 'пользователи бота'

    def __str__(self):
        return self.username
