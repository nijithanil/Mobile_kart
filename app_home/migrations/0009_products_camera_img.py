# Generated by Django 2.2.12 on 2022-03-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0008_auto_20220328_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='camera_img',
            field=models.ImageField(default='', upload_to='camera quality images'),
        ),
    ]
