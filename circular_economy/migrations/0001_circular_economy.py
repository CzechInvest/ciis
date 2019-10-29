# Generated by Django 2.2.3 on 2019-10-29 09:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name', max_length=40)),
                ('last_name', models.CharField(help_text='Last name', max_length=40)),
                ('middle_name', models.CharField(blank=True, help_text='Last name', max_length=40)),
                ('role', models.CharField(help_text='Director, HR Manager, ...', max_length=256)),
                ('crm', models.URLField(blank=True, help_text='CRM link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('activity', models.CharField(help_text='Activity name', max_length=200)),
                ('url', models.URLField()),
                ('characteristics', models.TextField()),
                ('project_description', models.TextField()),
                ('challange', models.TextField()),
                ('result', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='addresses.Address')),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='circular_economy.ContactPerson')),
                ('keywords', models.ManyToManyField(to='circular_economy.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('activity', models.CharField(help_text='Activity name', max_length=200)),
                ('url', models.URLField()),
                ('characteristics', models.TextField()),
                ('project_description', models.TextField()),
                ('challange', models.TextField()),
                ('result', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='addresses.Address')),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='circular_economy.ContactPerson')),
                ('keywords', models.ManyToManyField(to='circular_economy.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('url', models.URLField()),
                ('characteristics', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='addresses.Address')),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='circular_economy.ContactPerson')),
            ],
        ),
    ]
