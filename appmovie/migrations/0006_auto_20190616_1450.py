# Generated by Django 2.2.2 on 2019-06-16 14:50

import appmovie.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovie', '0005_auto_20190616_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to=appmovie.models.movie_directory_path),
        ),
    ]
