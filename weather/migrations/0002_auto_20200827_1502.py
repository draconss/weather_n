# Generated by Django 3.0.6 on 2020-08-27 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='city',
            name='code',
        ),
    ]