# Generated by Django 2.1.2 on 2018-10-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_details', '0009_auto_20181030_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant_details',
            name='location_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='restaurant_details',
            name='logo_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
