# Generated by Django 2.1.2 on 2018-11-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_details', '0022_auto_20181115_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='closing_hours',
            new_name='breakfast_hours',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='opening_hours',
            new_name='dinner_hours',
        ),
        migrations.AddField(
            model_name='setting',
            name='lunch_hours',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
