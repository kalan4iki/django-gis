# Generated by Django 3.0 on 2019-12-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20191218_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersbot',
            name='email',
            field=models.EmailField(default=None, help_text='Почта', max_length=40, verbose_name='Почта пользователя'),
            preserve_default=False,
        ),
    ]
