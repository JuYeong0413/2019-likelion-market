# Generated by Django 2.0.13 on 2019-05-26 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_remove_item_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
