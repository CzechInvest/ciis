# Generated by Django 2.0.5 on 2018-07-31 12:53

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cigeo', '0002_genericnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Geometrie')),
                ('name', models.CharField(max_length=256)),
                ('iata', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='PublicTransportStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Geometrie')),
                ('name', models.CharField(max_length=256)),
                ('fclass', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='RailwayStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Geometrie')),
                ('name', models.CharField(max_length=256)),
                ('fclass', models.CharField(max_length=25)),
            ],
        ),
    ]