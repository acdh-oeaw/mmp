# Generated by Django 4.0.7 on 2022-11-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0001_initial'),
        ('archiv', '0040_alter_autor_id_alter_event_id_alter_keyword_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usecase',
            name='layer',
            field=models.ManyToManyField(blank=True, help_text='Select GeoJson Layers which should be related to this UseCase', related_name='use_case', to='layers.geojsonlayer', verbose_name='GeoJson Layers'),
        )
    ]
