# Generated by Django 3.2 on 2021-10-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0021_stelle_lemmata'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='lang',
            field=models.CharField(blank=True, default='lat', help_text='ISO-639 Code for the main language of the text', max_length=3, null=True, verbose_name='Language of the Text'),
        ),
    ]
