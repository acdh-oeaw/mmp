# Generated by Django 3.1.5 on 2021-01-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0006_stelle_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='varianten',
            field=models.TextField(blank=True, help_text="Varianten, bitte mit ';' trennen", null=True, verbose_name='Varianten'),
        ),
    ]
