# Generated by Django 2.1.2 on 2018-11-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_details', '0020_auto_20181113_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='closing_hours',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='opening_hours',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
