# Generated by Django 2.1.7 on 2019-02-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_auto_20190227_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.CharField(max_length=250, unique=True, verbose_name='course name'),
        ),
    ]