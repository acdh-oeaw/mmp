# Generated by Django 3.2 on 2021-10-18 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0024_alter_stelle_lemmata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='lang',
        ),
    ]