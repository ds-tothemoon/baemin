# Generated by Django 2.0.7 on 2018-07-11 07:58

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop_latlng'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='meta',
            field=jsonfield.fields.JSONField(blank=True),
        ),
    ]
