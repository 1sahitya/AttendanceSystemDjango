# Generated by Django 2.1.7 on 2019-02-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0023_auto_20190226_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='mark',
            field=models.BooleanField(),
        ),
    ]