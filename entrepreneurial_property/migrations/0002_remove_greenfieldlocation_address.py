# Generated by Django 2.0.5 on 2018-08-23 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurial_property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greenfieldlocation',
            name='address',
        ),
    ]