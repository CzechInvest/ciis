# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0009_auto_20171212_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='logo',
            field=models.ImageField(blank=True, help_text='Logo', null=True, upload_to='uploads/infrastrucutre/logos'),
        ),
    ]
