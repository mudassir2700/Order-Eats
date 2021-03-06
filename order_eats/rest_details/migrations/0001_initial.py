# Generated by Django 2.1.2 on 2018-10-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('zipcode', models.PositiveIntegerField(max_length=20)),
                ('cuisine_type', models.CharField(choices=[('ITL', 'Italian'), ('MEX', 'Mexican'), ('CHI', 'Chinese'), ('MUG', 'Mughlai'), ('ALL', 'All Cuisine')], default='ALL', max_length=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
