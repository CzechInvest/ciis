# Generated by Django 3.1.1 on 2021-02-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databazeci', '0008_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]