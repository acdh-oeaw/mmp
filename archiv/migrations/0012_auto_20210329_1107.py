# Generated by Django 3.1.5 on 2021-03-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0011_auto_20210329_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='name_gr',
            field=models.CharField(blank=True, help_text='Name (gr)', max_length=250, verbose_name='Name (gr)'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='name_gr',
            field=models.CharField(blank=True, help_text='Name (gr)', max_length=250, verbose_name='Name (gr)'),
        ),
        migrations.AddField(
            model_name='ort',
            name='name_gr',
            field=models.CharField(blank=True, help_text='Name (gr)', max_length=250, verbose_name='Name (gr)'),
        ),
    ]
