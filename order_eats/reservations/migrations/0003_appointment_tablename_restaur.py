# Generated by Django 2.1.2 on 2018-11-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_appointment_table_restaur'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='tablename_restaur',
            field=models.CharField(default='Default Restaurant', max_length=20),
        ),
    ]
