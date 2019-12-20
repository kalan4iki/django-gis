# Generated by Django 3.0 on 2019-12-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_auto_20191219_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='MKDhistor',
            fields=[
                ('date', models.CharField(help_text='Дата отчета.', max_length=20, primary_key=True, serialize=False, verbose_name='Дата')),
                ('day', models.IntegerField(help_text='День.', verbose_name='День')),
                ('month', models.IntegerField(help_text='Месяц.', verbose_name='Месяц')),
                ('year', models.IntegerField(help_text='Год.', verbose_name='Год')),
                ('maxdvor', models.IntegerField(help_text='Всего МКД.', verbose_name='Всего МКД')),
                ('complete', models.IntegerField(help_text='Выполнено МКД.', verbose_name='Выполнено МКД')),
                ('proc', models.IntegerField(help_text='Процент МКД.', verbose_name='Процент МКД')),
                ('times', models.DateTimeField(auto_now=True, help_text='Время отчета.', verbose_name='Время')),
            ],
            options={
                'verbose_name': 'отчет по осмотру МКД',
                'verbose_name_plural': 'отчеты по осмотру МКД',
                'ordering': ['year', 'month', 'day'],
            },
        ),
    ]