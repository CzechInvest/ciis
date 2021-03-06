# Generated by Django 2.2.3 on 2019-12-27 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competence', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='KodSed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=16)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod_nci_07_13', models.CharField(blank=True, max_length=16, null=True, verbose_name='kód NČI 07-13')),
                ('npr_envi', models.BooleanField(blank=True, null=True, verbose_name='NPR/ENVI')),
                ('c_s', models.CharField(blank=True, choices=[('c', 'C'), ('s', 'S')], max_length=1, null=True, verbose_name='C/S')),
                ('fond', models.CharField(blank=True, choices=[('efrr_fs', 'EFRR / FS'), ('enrf', 'ENRF'), ('esf', 'ESF'), ('esf_yei', 'ESF / YEI'), ('eus', 'EUS'), ('ezfrv', 'EZFRV')], max_length=16, null=True, verbose_name='Fond')),
                ('kod_ek', models.CharField(blank=True, max_length=16, null=True)),
                ('wf', models.IntegerField(blank=True, null=True, verbose_name='WF')),
                ('kod_nci_2014', models.CharField(blank=True, max_length=16, null=True, verbose_name='KódNČI2014+')),
                ('kod_sfc', models.CharField(blank=True, max_length=16, null=True, verbose_name='Kód v SFC')),
                ('indicator_name_cs', models.TextField(verbose_name='Název indikátoru (CS)')),
                ('indicator_name_en', models.TextField(verbose_name='Název indikátoru (EN)')),
                ('unit', models.CharField(max_length=8, verbose_name='Měrná jednotka')),
                ('type', models.CharField(choices=[('context', 'Kontext'), ('output', 'Výstup'), ('result', 'Výsledek')], max_length=8, verbose_name='Typ')),
                ('definition', models.TextField(verbose_name='Definice')),
                ('frequency', models.CharField(max_length=16, verbose_name='Frekvence')),
                ('resource', models.URLField(blank=True, null=True, verbose_name='Odkaz na zdroj dat')),
                ('resource_comments', models.CharField(blank=True, max_length=256, null=True, verbose_name='Zdroj metodiky / komentáře')),
                ('es_esf2014', models.BooleanField(blank=True, null=True, verbose_name='Přenos do IS ESF2014+')),
                ('projects_number', models.IntegerField(blank=True, null=True, verbose_name='Počet Projektů')),
                ('ec_comments', models.TextField(blank=True, null=True, verbose_name='Comments EK')),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dotacni_matice.DataSource', verbose_name='Zdroj dat (Ž/P, ŘO, statistika')),
                ('field', models.ManyToManyField(blank=True, to='dotacni_matice.Field', verbose_name='Oblast')),
                ('kod_sed', models.ManyToManyField(blank=True, to='dotacni_matice.KodSed', verbose_name='Kód SED')),
                ('main_indicator', models.ManyToManyField(blank=True, related_name='indicator_main_indicator', to='dotacni_matice.OP', verbose_name='Hlavní indikátor')),
                ('op', models.ManyToManyField(blank=True, related_name='indicator_op', to='dotacni_matice.OP', verbose_name='OP')),
                ('sfc', models.ManyToManyField(blank=True, to='dotacni_matice.OP', verbose_name='SFC')),
            ],
        ),
        migrations.CreateModel(
            name='DotacniTitul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed', models.DateField(auto_now=True, help_text='Changed')),
                ('name', models.CharField(max_length=256)),
                ('area', models.CharField(blank=True, max_length=64, null=True)),
                ('mip', models.IntegerField(blank=True, choices=[(10, 10), (15, 15), (20, 20), (30, 30), (30, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95), (100, 100), (1, 'Ano'), (-1, 'Není stanoveno'), (-2, 'Dle aktivity'), (-3, 'Nelze určit')], null=True)),
                ('mp', models.IntegerField(blank=True, choices=[(10, 10), (15, 15), (20, 20), (30, 30), (30, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95), (100, 100), (1, 'Ano'), (-1, 'Není stanoveno'), (-2, 'Dle aktivity'), (-3, 'Nelze určit')], null=True)),
                ('sp', models.IntegerField(blank=True, choices=[(10, 10), (15, 15), (20, 20), (30, 30), (30, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95), (100, 100), (1, 'Ano'), (-1, 'Není stanoveno'), (-2, 'Dle aktivity'), (-3, 'Nelze určit')], null=True)),
                ('vp', models.IntegerField(blank=True, choices=[(10, 10), (15, 15), (20, 20), (30, 30), (30, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95), (100, 100), (1, 'Ano'), (-1, 'Není stanoveno'), (-2, 'Dle aktivity'), (-3, 'Nelze určit')], null=True)),
                ('nno', models.IntegerField(blank=True, choices=[(10, 10), (15, 15), (20, 20), (30, 30), (30, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95), (100, 100), (1, 'Ano'), (-1, 'Není stanoveno'), (-2, 'Dle aktivity'), (-3, 'Nelze určit')], null=True)),
                ('public', models.IntegerField(blank=True, choices=[(10, 10), (15, 15), (20, 20), (30, 30), (30, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95), (100, 100), (1, 'Ano'), (-1, 'Není stanoveno'), (-2, 'Dle aktivity'), (-3, 'Nelze určit')], null=True)),
                ('date_call', models.DateField(blank=True, null=True)),
                ('date_pref_from', models.DateField(blank=True, null=True)),
                ('date_pref_to', models.DateField(blank=True, null=True)),
                ('date_full_from', models.DateField(blank=True, null=True)),
                ('date_full_to', models.DateField(blank=True, null=True)),
                ('allocated', models.IntegerField(blank=True, help_text='[*10^6 Kč]', null=True)),
                ('min', models.IntegerField(blank=True, help_text='[*10^6 Kč]', null=True)),
                ('max', models.IntegerField(blank=True, help_text='[*10^6 Kč]', null=True)),
                ('form', models.CharField(blank=True, max_length=32, null=True)),
                ('history', models.CharField(blank=True, max_length=32, null=True)),
                ('regime', models.CharField(blank=True, max_length=32, null=True)),
                ('supported_activities', models.TextField(blank=True, null=True)),
                ('eligible_costs', models.TextField(blank=True, null=True)),
                ('ineligible_costs', models.TextField(blank=True, null=True)),
                ('pkn', models.IntegerField(blank=True, null=True)),
                ('pkv', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('afc', models.BooleanField(blank=True, null=True)),
                ('ipo', models.BooleanField(blank=True, null=True)),
                ('investment', models.BooleanField(blank=True, null=True)),
                ('noninvestment', models.BooleanField(blank=True, null=True)),
                ('remuneration', models.BooleanField(blank=True, null=True)),
                ('personal_costs', models.BooleanField(blank=True, null=True)),
                ('education', models.BooleanField(blank=True, null=True)),
                ('consultation', models.BooleanField(blank=True, null=True)),
                ('research', models.BooleanField(blank=True, null=True)),
                ('property', models.BooleanField(blank=True, null=True)),
                ('machines', models.BooleanField(blank=True, null=True)),
                ('construction', models.BooleanField(blank=True, null=True)),
                ('administration', models.BooleanField(blank=True, null=True)),
                ('hw', models.BooleanField(blank=True, null=True)),
                ('sw', models.BooleanField(blank=True, null=True)),
                ('lump', models.BooleanField(blank=True, null=True)),
                ('marketing', models.BooleanField(blank=True, null=True)),
                ('competence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dotacni_matice.Competence')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dotacni_matice.Program')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dotacni_matice.CallType')),
            ],
        ),
    ]
