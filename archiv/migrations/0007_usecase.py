# Generated by Django 3.1.5 on 2021-02-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0006_auto_20210223_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='UseCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Title of the Use Case', max_length=250, verbose_name='Title')),
                ('principal_investigator', models.CharField(blank=True, help_text='Principal Investigator of the Use Case', max_length=250, verbose_name='PI')),
                ('pi_norm_id', models.CharField(blank=True, help_text='e.g. GND-ID or ORCID', max_length=250, verbose_name='Some Norm-ID of the PI')),
                ('description', models.TextField(blank=True, help_text='Short Description of the Use Case', null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Use Case',
                'ordering': ['title'],
            },
        ),
    ]
