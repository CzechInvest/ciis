# Generated by Django 3.0.6 on 2020-09-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databazeci', '0002_subdomains'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subdomain',
            old_name='sector',
            new_name='subdomain',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='contact',
        ),
        migrations.AddField(
            model_name='subject',
            name='contact',
            field=models.ManyToManyField(to='databazeci.Contact'),
        ),
    ]