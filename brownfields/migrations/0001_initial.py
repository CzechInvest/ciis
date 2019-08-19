# Generated by Django 2.0.5 on 2019-06-26 12:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brownfield',
            fields=[
                ('id', models.IntegerField(default=-1, primary_key=True, serialize=False)),
                ('status', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('total_area', models.FloatField()),
                ('built_up_area', models.FloatField()),
                ('available_area', models.FloatField()),
                ('is_partible', models.BooleanField()),
                ('available_from', models.DateField()),
                ('currency', models.CharField(max_length=16)),
                ('selling_price_from', models.FloatField()),
                ('selling_price_to', models.FloatField()),
                ('rent_price_from', models.FloatField()),
                ('rent_price_to', models.FloatField()),
                ('access_road', models.TextField()),
                ('telco_kw_medium_distance', models.FloatField()),
            ],
            options={
                'verbose_name': 'Brownfield',
                'verbose_name_plural': 'Brownfieldy',
                'db_table': 'domino"."brownfields',
                'managed': False,
            },
        ),
    ]