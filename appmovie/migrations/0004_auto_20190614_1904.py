# Generated by Django 2.2.2 on 2019-06-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovie', '0003_auto_20190614_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=None),
        ),
    ]
