# Generated by Django 4.2.1 on 2023-06-23 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_order_payment_method_alter_order_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
