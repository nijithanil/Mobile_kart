# Generated by Django 2.2.12 on 2022-03-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0011_auto_20220328_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='model_ram',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
