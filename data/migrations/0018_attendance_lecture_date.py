# Generated by Django 2.1.7 on 2019-02-25 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='lecture_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]