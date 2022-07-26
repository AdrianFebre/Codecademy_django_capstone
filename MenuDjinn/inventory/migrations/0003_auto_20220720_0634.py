# Generated by Django 2.2.5 on 2022-07-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220720_0558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='unit',
            new_name='units',
        ),
        migrations.AddField(
            model_name='reciperequirements',
            name='ingredient_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]