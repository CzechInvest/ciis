# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0002_auto_20171121_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='cooperation',
            field=models.ManyToManyField(blank=True, null=True, to='infrastructure.Organisation'),
        ),
    ]
