# Generated by Django 2.2.2 on 2019-06-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovie', '0012_auto_20190617_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieraiting',
            name='comment',
            field=models.IntegerField(default=None),
        ),
    ]
