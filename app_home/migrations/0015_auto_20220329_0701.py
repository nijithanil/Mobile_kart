# Generated by Django 2.2.12 on 2022-03-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0014_auto_20220329_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='model_RAM',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='model_ROM',
            field=models.CharField(default='', max_length=100),
        ),
    ]
