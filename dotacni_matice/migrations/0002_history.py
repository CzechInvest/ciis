# Generated by Django 2.2.3 on 2019-12-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotacni_matice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dotacnititul',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
    ]
