# Generated by Django 2.1.2 on 2018-11-24 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_auto_20181125_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='ord_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
