# Generated by Django 2.2.2 on 2019-06-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovie', '0021_auto_20190617_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieraiting',
            name='vote',
            field=models.FloatField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
    ]
