# Generated by Django 2.2.12 on 2022-03-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0004_auto_20220328_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.ImageField(default='', upload_to='brand logo'),
        ),
    ]
