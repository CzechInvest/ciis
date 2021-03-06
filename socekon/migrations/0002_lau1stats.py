# Generated by Django 2.0.5 on 2018-12-19 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cigeo', '0003_airport_publictransportstop_railwaystation'),
        ('socekon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lau1Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('population', models.IntegerField(verbose_name='Population')),
                ('work_power', models.IntegerField(verbose_name='Work power')),
                ('unemployment', models.IntegerField(verbose_name='Unemployment')),
                ('unemployment_rate', models.FloatField(verbose_name='Unemployment rate')),
                ('unemployed_per_job', models.FloatField(verbose_name='Medium salary')),
                ('medium_salary', models.IntegerField(verbose_name='Medium salary')),
                ('lau1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cigeo.Lau1')),
            ],
        ),
    ]
