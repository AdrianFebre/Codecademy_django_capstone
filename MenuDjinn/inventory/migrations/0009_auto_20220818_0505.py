# Generated by Django 2.2.5 on 2022-08-18 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20220804_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimedStrings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=50)),
                ('timestamp', models.DateField(default=datetime.datetime(2022, 8, 18, 5, 5, 6, 569761))),
            ],
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_timestamp',
            field=models.DateField(default=datetime.datetime(2022, 8, 18, 5, 5, 6, 569387)),
        ),
    ]
