# Generated by Django 3.1.5 on 2021-03-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0010_auto_20210226_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='alt_title',
            field=models.CharField(blank=True, help_text='Alternative(r) Titel', max_length=250, verbose_name='Alternative(r) Titel'),
        ),
        migrations.AddField(
            model_name='text',
            name='text_lang',
            field=models.CharField(blank=True, default='lat', help_text="Spraches des Textes, default 'lat'", max_length=250, verbose_name='Sprache des Textes'),
        ),
    ]
