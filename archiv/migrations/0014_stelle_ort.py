# Generated by Django 3.1.5 on 2021-03-29 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0013_keyword_related_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='stelle',
            name='ort',
            field=models.ForeignKey(blank=True, help_text='Ort', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_stelle_ort_ort', to='archiv.ort', verbose_name='Ort'),
        ),
    ]