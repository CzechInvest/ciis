# Generated by Django 2.0.5 on 2018-08-23 19:44

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('cigeo', '0003_airport_publictransportstop_railwaystation'),
        ('entrepreneurial_property', '0007_auto_20180823_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrownfieldAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Description', null=True)),
                ('attachment', models.FileField(help_text='Attachment file', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldDrinkWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('diameter', models.IntegerField(blank=True, help_text='<code>[mm]</code>', null=True, verbose_name='Diameter')),
                ('capacity', models.IntegerField(blank=True, help_text='Capacity <code>[m<sup>3</sup>/d]</code>', verbose_name='Capacity')),
                ('well', models.BooleanField(verbose_name='Well')),
                ('well_capacity', models.IntegerField(blank=True, help_text='Well capacity <code>[m<sup>3</sup>/d]</code>', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldElectricity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('current', models.IntegerField(blank=True, help_text='Napětí <code>[kV]</code>', verbose_name='Napětí')),
                ('capacity', models.IntegerField(help_text='Kapacita <code>[MW]</code>', verbose_name='Kapacita')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldGas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('diameter', models.IntegerField(blank=True, help_text='<code>[mm]</code>', null=True, verbose_name='Diameter')),
                ('pressure', models.IntegerField(blank=True, help_text='Pressure <code>[kPa]</code>', verbose_name='Pressure')),
                ('capacity', models.IntegerField(blank=True, help_text='Capacity <code>[m<sup>3</sup>/d]</code>', verbose_name='Capacity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldGenericNote',
            fields=[
                ('genericnote_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cigeo.GenericNote')),
            ],
            bases=('cigeo.genericnote',),
        ),
        migrations.CreateModel(
            name='BrownfieldLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='Body, linie, polygony', null=True, srid=4326, verbose_name='Geometrie')),
                ('highway_distance', models.FloatField(default=-1)),
                ('airport_distance', models.FloatField(default=-1)),
                ('public_transport_distance', models.FloatField(default=-1)),
                ('railway_distance', models.FloatField(default=-1)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='addresses.Address', verbose_name='Adresa')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Photo title', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Description', null=True)),
                ('image', models.ImageField(help_text='Image file', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldTechnologicalWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('diameter', models.IntegerField(blank=True, help_text='<code>[mm]</code>', null=True, verbose_name='Diameter')),
                ('capacity', models.IntegerField(blank=True, help_text='Capacity <code>[m<sup>3</sup>/d]</code>', verbose_name='Capacity')),
                ('well', models.BooleanField(verbose_name='Well')),
                ('well_capacity', models.IntegerField(blank=True, help_text='Well capacity <code>[m<sup>3</sup>/d]</code>', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldTelecommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('technology', models.CharField(blank=True, choices=[('optic', 'Optic'), ('metalic', 'Metalic'), ('wifi', 'WIFI'), ('cell', 'Cellular')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldWasteWaterIndustrial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('diameter', models.IntegerField(blank=True, help_text='Velikost přípojky <code>[mm]</code>', verbose_name='Průměr')),
                ('capacity', models.IntegerField(blank=True, help_text='Kapacita přípojky <code>[m<sup>3</sup>/d]</code>', verbose_name='Kapacita přípojky')),
                ('sewage_plant_name', models.TextField(blank=True, help_text='Name and address')),
                ('sewage_plant_technology', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldWasteWaterRain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('diameter', models.IntegerField(blank=True, help_text='Velikost přípojky <code>[mm]</code>', verbose_name='Průměr')),
                ('capacity', models.IntegerField(blank=True, help_text='Kapacita přípojky <code>[m<sup>3</sup>/d]</code>', verbose_name='Kapacita přípojky')),
                ('absorbtion', models.CharField(blank=True, help_text='River name, where the water will be absorbed', max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrownfieldWasteWaterSevage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('diameter', models.IntegerField(blank=True, help_text='Velikost přípojky <code>[mm]</code>', verbose_name='Průměr')),
                ('capacity', models.IntegerField(blank=True, help_text='Kapacita přípojky <code>[m<sup>3</sup>/d]</code>', verbose_name='Kapacita přípojky')),
                ('sewage_plant_name', models.TextField(blank=True, help_text='Name and address')),
                ('sewage_plant_technology', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Description', null=True)),
                ('attachment', models.FileField(help_text='Attachment file', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkDrinkWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkElectricity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkGas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkGenericNote',
            fields=[
                ('genericnote_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cigeo.GenericNote')),
            ],
            bases=('cigeo.genericnote',),
        ),
        migrations.CreateModel(
            name='ScientificParkLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='Body, linie, polygony', null=True, srid=4326, verbose_name='Geometrie')),
                ('highway_distance', models.FloatField(default=-1)),
                ('airport_distance', models.FloatField(default=-1)),
                ('public_transport_distance', models.FloatField(default=-1)),
                ('railway_distance', models.FloatField(default=-1)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='addresses.Address', verbose_name='Adresa')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Photo title', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Description', null=True)),
                ('image', models.ImageField(help_text='Image file', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkTechnologicalWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkTelecommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('technology', models.CharField(blank=True, choices=[('optic', 'Optic'), ('metalic', 'Metalic'), ('wifi', 'WIFI'), ('cell', 'Cellular')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkWasteWaterIndustrial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('sewage_plant_name', models.TextField(blank=True, help_text='Name and address')),
                ('sewage_plant_technology', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkWasteWaterRain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('absorbtion', models.CharField(blank=True, help_text='River name, where the water will be absorbed', max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScientificParkWasteWaterSevage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0, help_text='Dinstance to object <code>[m]</code>', verbose_name='Distnace')),
                ('note', models.TextField(blank=True, help_text='Note', verbose_name='Note')),
                ('sewage_plant_name', models.TextField(blank=True, help_text='Name and address')),
                ('sewage_plant_technology', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='air_condition',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='available_since',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='canteen',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='category',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='crane',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='fire_protection',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='heating',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='height',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='load_lift',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='other_equipment',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='parking_place',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='personal_lift',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='reception_desk',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='security',
        ),
        migrations.RemoveField(
            model_name='brownfield',
            name='service_price',
        ),
        migrations.RemoveField(
            model_name='office',
            name='parcel_numbers',
        ),
        migrations.RemoveField(
            model_name='scientificpark',
            name='access_road',
        ),
        migrations.RemoveField(
            model_name='scientificpark',
            name='railway_siding',
        ),
        migrations.AlterField(
            model_name='brownfield',
            name='description',
            field=models.TextField(help_text='Description'),
        ),
        migrations.AlterField(
            model_name='brownfield',
            name='parcel_numbers',
            field=models.CharField(help_text='Parcel numbers', max_length=255),
        ),
        migrations.AddField(
            model_name='scientificparkwastewatersevage',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparkwastewaterrain',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparkwastewaterindustrial',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparktelecommunication',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparktechnologicalwater',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparkphoto',
            name='green_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparklocation',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparkgenericnote',
            name='green_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparkgas',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparkelectricity',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparkdrinkwater',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='scientificparkattachment',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.ScientificPark'),
        ),
        migrations.AddField(
            model_name='brownfieldwastewatersevage',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldwastewaterrain',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldwastewaterindustrial',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldtelecommunication',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldtechnologicalwater',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldphoto',
            name='green_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldlocation',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldgenericnote',
            name='green_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldgas',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldelectricity',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfielddrinkwater',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
        migrations.AddField(
            model_name='brownfieldattachment',
            name='green_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurial_property.Brownfield'),
        ),
    ]
