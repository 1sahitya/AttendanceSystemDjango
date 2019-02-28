# Generated by Django 2.1.7 on 2019-02-20 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=250)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.Course')),
            ],
        ),
    ]