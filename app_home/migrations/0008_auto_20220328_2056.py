# Generated by Django 2.2.12 on 2022-03-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0007_auto_20220328_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='desc',
        ),
        migrations.AddField(
            model_name='products',
            name='product_desc',
            field=models.TextField(default=''),
        ),
    ]
