# Generated by Django 2.0.5 on 2019-01-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoiswho', '0003_whoiswho_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactperson',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactperson',
            name='phone',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='institution',
            name='ico',
            field=models.CharField(max_length=8),
        ),
    ]
