# Generated by Django 2.2.5 on 2022-07-31 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20220731_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_timestamp',
            field=models.DateField(default=datetime.datetime(2022, 7, 31, 5, 8, 18, 388374)),
        ),
    ]
