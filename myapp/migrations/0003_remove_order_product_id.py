# Generated by Django 2.0 on 2021-05-27 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210527_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Product_id',
        ),
    ]
