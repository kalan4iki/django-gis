# Generated by Django 3.0 on 2019-12-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_auto_20191224_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mkdhistor',
            name='day',
            field=models.IntegerField(blank=True, help_text='День.', null=True, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='mkdhistor',
            name='month',
            field=models.IntegerField(blank=True, help_text='Месяц.', null=True, verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='mkdhistor',
            name='year',
            field=models.IntegerField(blank=True, help_text='Год.', null=True, verbose_name='Год'),
        ),
    ]
