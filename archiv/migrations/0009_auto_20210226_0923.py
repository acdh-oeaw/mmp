# Generated by Django 3.1.5 on 2021-02-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0008_stelle_use_case'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='edition',
        ),
        migrations.AddField(
            model_name='text',
            name='edition',
            field=models.CharField(blank=True, help_text='Edition', max_length=350, verbose_name='Edition'),
        ),
        migrations.DeleteModel(
            name='Edition',
        ),
    ]
