# Generated by Django 4.2.1 on 2023-06-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='+123 45 678 90 12', max_length=256, verbose_name='Phone'),
        ),
    ]
