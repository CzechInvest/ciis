# Generated by Django 2.2.3 on 2019-12-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotacni_matice', '0004_regime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='program',
            field=models.CharField(max_length=32),
        ),
    ]