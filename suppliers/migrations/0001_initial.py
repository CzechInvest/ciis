# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Certifikát', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Sektor', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Název dodavatele', max_length=200)),
                ('regid', models.IntegerField(help_text='IČO')),
                ('phone', models.CharField(help_text='Telefon', max_length=20)),
                ('fax', models.CharField(help_text='Fax', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('join_venture', models.BooleanField(default=False, help_text='Join-venture')),
                ('custom_made', models.BooleanField(default=False, help_text='Zakázková výroa')),
                ('capital', models.BooleanField(default=False, help_text='Zahraniční kapitál')),
                ('turnover', models.IntegerField(help_text='Obrat [€]')),
                ('export', models.FloatField(help_text='Export [%]')),
                ('employes', models.IntegerField(help_text='Počet zaměstnanců')),
                ('year', models.IntegerField(help_text='Rok založení')),
                ('main_activity', models.CharField(help_text='Hlavní činnost', max_length=200)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.Address')),
                ('certificates', models.ManyToManyField(to='suppliers.Certificate')),
                ('contact_person', models.ManyToManyField(to='contacts.ContactPerson')),
                ('sectors', models.ManyToManyField(to='suppliers.Sector')),
            ],
        ),
    ]
