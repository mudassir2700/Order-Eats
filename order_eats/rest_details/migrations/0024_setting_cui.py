# Generated by Django 2.1.2 on 2018-11-15 13:30

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rest_details', '0023_auto_20181115_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='cui',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ITALIANL', 'Italian'), ('MEXICAN', 'Mexican'), ('CHINESE', 'Chinese'), ('MUGHLAI', 'Mughlai'), ('MULTICUISINE', 'MULTICUISINE')], max_length=45, null=True),
        ),
    ]
