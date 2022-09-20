# Generated by Django 3.2.9 on 2022-06-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0036_spatialcoverage_show_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='usecase',
            name='custom_layer',
            field=models.CharField(blank=True, help_text="This name needs to match a specific layer name,            e.g '800' to load a layer '800'", max_length=250, null=True, verbose_name='Name of additional Layer'),
        ),
    ]