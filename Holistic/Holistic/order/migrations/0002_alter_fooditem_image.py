# Generated by Django 4.1 on 2022-08-22 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(default='', upload_to='order/images'),
        ),
    ]