# Generated by Django 3.1.5 on 2021-01-29 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vocabs', '0001_initial'),
    ]

    operations = [
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
            ],
            options={
                'verbose_name': 'Autor',
                'ordering': ['legacy_pk'],
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('zitat', models.CharField(blank=True, help_text='Zitat', max_length=250, verbose_name='Zitat')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
            ],
            options={
                'verbose_name': 'Edition',
                'ordering': ['zitat'],
            },
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='Primärschlüssel Alt', null=True, verbose_name='Primärschlüssel Alt')),
                ('stichwort', models.CharField(blank=True, help_text='Stichwort', max_length=250, verbose_name='Stichwort')),
                ('art', models.CharField(blank=True, help_text='Art des Stichworts', max_length=250, verbose_name='Art des Stichworts')),
                ('varianten', models.TextField(blank=True, help_text="Varianten, bitte mit ';' trennen", null=True, verbose_name='Varianten')),
                ('wurzel', models.CharField(blank=True, help_text='Wurzel', max_length=250, verbose_name='Wurzel')),
                ('kommentar', models.TextField(blank=True, help_text='Kommentar', null=True, verbose_name='Kommentar')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
            ],
            options={
                'verbose_name': 'Keyword',
                'ordering': ['stichwort'],
            },
        ),
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
                ('long', models.FloatField(blank=True, help_text='Längengrad', null=True, verbose_name='Längengrad')),
                ('lat', models.FloatField(blank=True, help_text='Breitengrad', null=True, verbose_name='Breitengrad')),
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
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='Primärschlüssel Alt', null=True, verbose_name='Primärschlüssel Alt')),
                ('title', models.CharField(blank=True, help_text='Titel', max_length=250, verbose_name='Titel')),
                ('jahrhundert', models.CharField(blank=True, help_text='Jahrhundert', max_length=250, verbose_name='Jahrundert')),
                ('start_date', models.CharField(blank=True, help_text='von', max_length=250, verbose_name='von')),
                ('end_date', models.CharField(blank=True, help_text='bis', max_length=250, verbose_name='bis')),
                ('kommentar', models.TextField(blank=True, help_text='Kommentar', null=True, verbose_name='Kommentar')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('art', models.ForeignKey(blank=True, help_text='Textart', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_text_art_skosconcept', to='vocabs.skosconcept', verbose_name='Textart')),
                ('autor', models.ManyToManyField(blank=True, help_text='Autor', related_name='rvn_text_autor_autor', to='archiv.Autor', verbose_name='Autor')),
                ('edition', models.ManyToManyField(blank=True, help_text='Edition', related_name='rvn_text_edition_edition', to='archiv.Edition', verbose_name='Edition')),
                ('ort', models.ManyToManyField(blank=True, help_text='Ort', related_name='rvn_text_ort_ort', to='archiv.Ort', verbose_name='Ort')),
            ],
            options={
                'verbose_name': 'Text',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Stelle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='Primärschlüssel Alt', null=True, verbose_name='Primärschlüssel Alt')),
                ('summary', models.TextField(blank=True, help_text='Zusammenfassung', null=True, verbose_name='Zusammenfassung')),
                ('zitat', models.TextField(blank=True, help_text='Zitat', null=True, verbose_name='Zitat')),
                ('translation', models.TextField(blank=True, help_text='Übersetzung', null=True, verbose_name='Übersetzung')),
                ('kommentar', models.TextField(blank=True, help_text='Kommentar', null=True, verbose_name='Kommentar')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('key_word', models.ManyToManyField(blank=True, help_text='Stichwort', related_name='rvn_stelle_key_word_keyword', to='archiv.KeyWord', verbose_name='Stichwort')),
                ('text', models.ForeignKey(blank=True, help_text='Text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_stelle_text_text', to='archiv.text', verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Stelle',
                'ordering': ['legacy_pk'],
            },
        ),
        migrations.AddField(
            model_name='autor',
            name='ort',
            field=models.ForeignKey(blank=True, help_text='Ort', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_autor_ort_ort', to='archiv.ort', verbose_name='Ort'),
        ),
    ]
