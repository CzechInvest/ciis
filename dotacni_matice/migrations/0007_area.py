# Generated by Django 2.2.3 on 2019-12-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotacni_matice', '0006_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dotacnititul',
            name='area',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='program',
            field=models.CharField(max_length=64),
        ),
    ]
