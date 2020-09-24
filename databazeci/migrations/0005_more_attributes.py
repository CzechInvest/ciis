# Generated by Django 3.0.6 on 2020-09-24 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('databazeci', '0004_more_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='business_area',
            field=models.ManyToManyField(blank=True, to='databazeci.BusinessArea'),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='department',
        ),
        migrations.AddField(
            model_name='subject',
            name='department',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='databazeci.Department'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='domain',
            field=models.ManyToManyField(blank=True, to='databazeci.Domain'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='ket',
            field=models.ManyToManyField(blank=True, to='databazeci.Ket'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='databazeci.Keyword'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='nace',
            field=models.ManyToManyField(blank=True, to='databazeci.Nace'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subdomain',
            field=models.ManyToManyField(blank=True, to='databazeci.Subdomain'),
        ),
    ]