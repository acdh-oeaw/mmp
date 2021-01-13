# Generated by Django 3.1.5 on 2021-01-12 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vocabs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='Primärschlüssel Alt', null=True, verbose_name='Primärschlüssel Alt')),
                ('name', models.CharField(blank=True, help_text='Name (en)', max_length=250, verbose_name='Name (en)')),
                ('name_antik', models.CharField(blank=True, help_text='Name (antik)', max_length=250, verbose_name='Name (antik)')),
                ('name_de', models.CharField(blank=True, help_text='Name (de)', max_length=250, verbose_name='Name (de)')),
                ('name_fr', models.CharField(blank=True, help_text='Name (fr)', max_length=250, verbose_name='Name (fr)')),
                ('name_it', models.CharField(blank=True, help_text='Name (it)', max_length=250, verbose_name='Name (it)')),
                ('kommentar', models.TextField(blank=True, help_text='Kommentar', null=True, verbose_name='Kommentar')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('art', models.ForeignKey(blank=True, help_text='Art des Ortes', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_ort_art_skosconcept', to='vocabs.skosconcept', verbose_name='Art des Ortes')),
                ('kategorie', models.ForeignKey(blank=True, help_text='Kategorie des Ortes', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_ort_kategorie_skosconcept', to='vocabs.skosconcept', verbose_name='Kategorie des Ortes')),
            ],
            options={
                'verbose_name': 'Ort',
                'ordering': ['legacy_pk'],
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='Primärschlüssel Alt', null=True, verbose_name='Primärschlüssel Alt')),
                ('name', models.CharField(blank=True, help_text='Name (de)', max_length=250, verbose_name='Name (de)')),
                ('name_lat', models.CharField(blank=True, help_text='Name (lat)', max_length=250, verbose_name='Name (lat)')),
                ('name_en', models.CharField(blank=True, help_text='Name (en)', max_length=250, verbose_name='Name (en)')),
                ('name_fr', models.CharField(blank=True, help_text='Name (fr)', max_length=250, verbose_name='Name (fr)')),
                ('name_it', models.CharField(blank=True, help_text='Name (it)', max_length=250, verbose_name='Name (it)')),
                ('jahrhundert', models.CharField(blank=True, help_text='Jahrhundert', max_length=250, verbose_name='Jahrundert')),
                ('start_date', models.CharField(blank=True, help_text='von', max_length=250, verbose_name='von')),
                ('end_date', models.CharField(blank=True, help_text='bis', max_length=250, verbose_name='bis')),
                ('kommentar', models.TextField(blank=True, help_text='Kommentar', null=True, verbose_name='Kommentar')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('ort', models.ForeignKey(blank=True, help_text='Ort', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_autor_ort_ort', to='archiv.ort', verbose_name='Ort')),
            ],
            options={
                'verbose_name': 'Autor',
                'ordering': ['legacy_pk'],
            },
        ),
    ]
