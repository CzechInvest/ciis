# Generated by Django 2.0.5 on 2018-08-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurial_property', '0008_auto_20180823_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='brownfield',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
