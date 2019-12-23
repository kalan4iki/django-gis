# Generated by Django 3.0 on 2019-12-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_auto_20191223_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kndhistor',
            name='completeproc',
            field=models.FloatField(help_text='Выполнено процентов.', verbose_name='Выполнено процентов'),
        ),
        migrations.AlterField(
            model_name='kndhistor',
            name='dostproc',
            field=models.FloatField(help_text='Доступно процентов.', verbose_name='Доступно процентов'),
        ),
        migrations.AlterField(
            model_name='kndhistor',
            name='netrebproc',
            field=models.FloatField(help_text='Не ребуются процентов.', verbose_name='Не ребуются процентов'),
        ),
        migrations.AlterField(
            model_name='kndhistor',
            name='vraboteproc',
            field=models.FloatField(help_text='В работе процентов.', verbose_name='В работе процентов'),
        ),
    ]