# Generated by Django 2.1.2 on 2018-11-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_details', '0032_auto_20181115_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant_details',
            name='cuisine_type',
        ),
        migrations.AddField(
            model_name='restaurant_details',
            name='Restaurant_Special_Items',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
