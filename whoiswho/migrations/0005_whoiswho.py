# Generated by Django 2.0.5 on 2019-05-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoiswho', '0004_whoiswho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='code',
            field=models.CharField(max_length=16),
        ),
    ]
