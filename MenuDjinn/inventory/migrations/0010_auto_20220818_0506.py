# Generated by Django 2.2.5 on 2022-08-18 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20220818_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_timestamp',
            field=models.DateField(default=datetime.datetime(2022, 8, 18, 5, 6, 32, 88480)),
        ),
        migrations.AlterField(
            model_name='timedstrings',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2022, 8, 18, 5, 6, 32, 88701)),
        ),
    ]
