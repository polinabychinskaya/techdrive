# Generated by Django 4.2.1 on 2023-06-24 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
