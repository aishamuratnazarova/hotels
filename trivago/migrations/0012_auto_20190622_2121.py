# Generated by Django 2.2 on 2019-06-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivago', '0011_auto_20190622_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='departure_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата отезда'),
        ),
    ]