# Generated by Django 2.1.2 on 2018-11-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0022_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_type',
            field=models.CharField(choices=[('veg_starter', 'Vegetarian Starter'), ('nonveg_starter', 'Nonveg Starter'), ('veg_maincourse', 'Vegetarian maincourse'), ('nonveg_maincourse', 'Nonveg maincourse'), ('dessert', 'Dessert'), ('Beverages', 'Beverages'), ('roti', 'Rotis'), ('veg_chinese', 'veg_chinese'), ('nonveg_chinese', 'nonveg_chinese'), ('wine', 'wine'), ('beer', 'beer'), ('vodka', 'vodka'), ('redwine', 'redwine'), ('pizza', 'pizza'), ('burger', 'burger')], default='Vegetarian maincourse', max_length=50),
        ),
    ]
