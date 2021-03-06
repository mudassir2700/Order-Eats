# Generated by Django 2.1.2 on 2018-11-15 17:23

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rest_details', '0030_auto_20181115_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='Cuisines_You_Offer',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='Pure_vegetarian',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='alcohol_served',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='buffet',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='buffet_timing',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='cost_for_two_people',
        ),
        migrations.AddField(
            model_name='restaurant_details',
            name='Cuisines_You_Offer',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ITALIANL', 'Italian'), ('MEXICAN', 'Mexican'), ('CHINESE', 'Chinese'), ('MUGHLAI', 'Mughlai'), ('North Indian', 'North Indian'), ('South Indian', 'South Indian'), ('Rolls', 'Rolls'), ('Kebabs', 'Kebabs'), ('Momos', 'Momos'), ('Fast Food', 'Fast Food'), ('Dessert', 'Dessert'), ('Ice-Cream', 'Ice-Cream')], max_length=105, null=True),
        ),
        migrations.AddField(
            model_name='restaurant_details',
            name='Pure_vegetarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant_details',
            name='alcohol_served',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant_details',
            name='buffet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant_details',
            name='buffet_timing',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant_details',
            name='cost_for_two_people',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
