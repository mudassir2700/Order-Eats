# Generated by Django 2.1.2 on 2018-11-22 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_cart_rest_cart_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='rest_cart_name',
            new_name='menu_name',
        ),
    ]
