# Generated by Django 2.1.5 on 2019-02-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20190220_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='student_pics/default.png', max_length=500, upload_to='student_pics/'),
        ),
    ]