# Generated by Django 2.0.13 on 2019-05-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20190526_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='avg_star',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='bought',
            field=models.IntegerField(default=0),
        ),
    ]
