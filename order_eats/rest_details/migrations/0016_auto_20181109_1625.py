# Generated by Django 2.1.2 on 2018-11-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_details', '0015_auto_20181109_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant_details',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_image/'),
        ),
    ]
