# Generated by Django 2.0.5 on 2019-01-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoiswho', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whoiswho',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
