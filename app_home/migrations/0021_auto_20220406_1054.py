# Generated by Django 2.2.12 on 2022-04-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0020_auto_20220406_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='off_prize',
            field=models.IntegerField(),
        ),
    ]