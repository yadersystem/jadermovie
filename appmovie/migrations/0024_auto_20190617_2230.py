# Generated by Django 2.2.2 on 2019-06-17 22:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appmovie', '0023_auto_20190617_2201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieraiting',
            options={'permissions': (('can_vote_two_times', 'Can vote two times'),)},
        ),
        migrations.AlterUniqueTogether(
            name='movieraiting',
            unique_together={('user', 'movie')},
        ),
    ]
