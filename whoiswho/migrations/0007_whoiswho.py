# Generated by Django 2.0.5 on 2019-05-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoiswho', '0006_whoiswho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactperson',
            name='phone',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]