# Generated by Django 3.1.1 on 2021-02-19 09:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_databazeci'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='address',
            name='addresses_a_adm_ac0e8f_idx',
        ),
        migrations.AlterField(
            model_name='address',
            name='adm',
            field=models.IntegerField(db_index=True, help_text='Kód ADM', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='house_number',
            field=models.CharField(db_index=True, default=None, help_text='Domovní číslo', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='orientation_number',
            field=models.CharField(db_index=True, default=None, help_text='Orientační číslo', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(db_index=True, help_text='Ulice', max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(db_index=True, help_text='PSČ', max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(db_index=True, help_text='Obec', max_length=200),
        ),
        migrations.AddIndex(
            model_name='address',
            index=models.Index(fields=['adm', 'street', 'orientation_number', 'city', 'zipcode', 'coordinates'], name='addresses_a_adm_0843ae_idx'),
        ),
    ]
