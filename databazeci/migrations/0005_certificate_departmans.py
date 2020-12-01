# Generated by Django 3.1.1 on 2020-12-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databazeci', '0004_sectors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(max_length=32)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='abbr',
        ),
        migrations.RemoveField(
            model_name='legalform',
            name='id',
        ),
        migrations.AlterField(
            model_name='legalform',
            name='form_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='subject',
            name='certificates',
            field=models.ManyToManyField(to='databazeci.Certificate'),
        ),
    ]
