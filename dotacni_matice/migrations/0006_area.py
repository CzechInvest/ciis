# Generated by Django 2.2.3 on 2019-12-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotacni_matice', '0005_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dotacnititul',
            name='area',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
