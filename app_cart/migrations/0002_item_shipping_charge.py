# Generated by Django 2.2.12 on 2022-04-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='shipping_charge',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]