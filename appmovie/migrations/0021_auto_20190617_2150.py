# Generated by Django 2.2.2 on 2019-06-17 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovie', '0020_auto_20190617_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieraiting',
            name='vote',
            field=models.FloatField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=None),
        ),
    ]
