# Generated by Django 2.2.12 on 2022-03-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0009_products_camera_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='MP_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='products',
            name='megha_pixel',
            field=models.CharField(default='', max_length=200),
        ),
    ]
