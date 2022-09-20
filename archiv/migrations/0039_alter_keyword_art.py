# Generated by Django 3.2.9 on 2022-06-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0038_alter_keyword_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='art',
            field=models.CharField(blank=True, choices=[('Keyword', 'Keyword'), ('Name', 'Name'), ('Ethnonym', 'Ethnonym'), ('Region', 'Region'), ('unclear', 'unclear')], help_text='Type of keyword', max_length=250, verbose_name='Type of keyword'),
        ),
    ]