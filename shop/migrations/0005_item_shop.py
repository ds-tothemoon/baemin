# Generated by Django 2.0.7 on 2018-07-11 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_item_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Shop'),
        ),
    ]