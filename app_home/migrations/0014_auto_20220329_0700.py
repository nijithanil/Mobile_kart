# Generated by Django 2.2.12 on 2022-03-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0013_auto_20220328_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand_image',
            field=models.ImageField(default='', upload_to='brand logo image'),
        ),
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.CharField(default='', max_length=100),
        ),
    ]