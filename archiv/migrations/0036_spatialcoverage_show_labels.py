# Generated by Django 3.2.9 on 2022-05-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0035_auto_20220328_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='spatialcoverage',
            name='show_labels',
            field=models.BooleanField(default=True, help_text='True if the label of the Spatial Coverage should be visible in the front end', verbose_name='Show Labels'),
        ),
    ]
