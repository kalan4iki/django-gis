from django.db import models
import uuid
# Create your models here.

class KNDhistor(models.Model): #Отчеты по территориям
    date = models.CharField(max_length=20, help_text='Дата отчета.',
                            verbose_name = 'Дата', primary_key = True)
    day = models.IntegerField(help_text='День.', verbose_name = 'День')
    month = models.IntegerField(help_text='Месяц.', verbose_name = 'Месяц')
    year = models.IntegerField(help_text='Год.', verbose_name = 'Год')
    maxdvor = models.IntegerField(help_text='Всего дворов.',
                            verbose_name = 'Всего дворов')
    complete = models.IntegerField(help_text='Выполнено дворов.',
                            verbose_name = 'Выполнено дворов')
    proc = models.IntegerField(help_text='Процент выполнения.',
                            verbose_name = 'Процент выполнения')
    times = models.CharField(max_length=20, help_text='Время отчета.',
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
    day = models.IntegerField(help_text='День.', verbose_name = 'День')
    month = models.IntegerField(help_text='Месяц.', verbose_name = 'Месяц')
    year = models.IntegerField(help_text='Год.', verbose_name = 'Год')
    maxdvor = models.IntegerField(help_text='Всего ДИП.',
                            verbose_name = 'Всего ДИП')
    complete = models.IntegerField(help_text='Выполнено ДИП.',
                            verbose_name = 'Выполнено ДИП')
    proc = models.IntegerField(help_text='Процент ДИП.',
                            verbose_name = 'Процент ДИП')
    times = models.CharField(max_length=20, help_text='Время отчета.',
                            verbose_name = 'Время')

    class Meta:
        ordering = ['year', 'month', 'day']
        verbose_name = 'отчет по осмотру ДИП'
        verbose_name_plural = 'отчеты по осмотру ДИП'

    def __str__(self):
        return self.date

class Usersbot(models.Model):
    username = models.CharField(max_length=20, help_text='username',
                            verbose_name = 'username')
    id = models.IntegerField(help_text='ID пользователя.', verbose_name = 'ID',
                            primary_key = True)
    email = models.EmailField(max_length=40, help_text='Почта',
                            verbose_name = 'Почта пользователя')
    last_name = models.CharField(max_length=20, help_text='Фамилия',
                            verbose_name = 'Фамилия', blank = True)
    first_name = models.CharField(max_length=20, help_text='Имя',
                            verbose_name = 'Имя', blank = True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, help_text='Статус регистрации',
                            verbose_name = 'Статус')
    role = models.CharField(max_length=20, help_text='Роль пользователя',
                            verbose_name = 'Роль')

    class Meta:
        ordering = ['username']
        verbose_name = 'пользователь бота'
        verbose_name_plural = 'пользователи бота'

    def __str__(self):
        return self.username
