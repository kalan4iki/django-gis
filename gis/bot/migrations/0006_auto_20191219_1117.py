# Generated by Django 3.0 on 2019-12-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20191218_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diphistor',
            name='times',
            field=models.DateTimeField(auto_now=True, help_text='Время отчета.', verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='kndhistor',
            name='times',
            field=models.DateTimeField(auto_now=True, help_text='Время отчета.', verbose_name='Время проверки'),
        ),
    ]