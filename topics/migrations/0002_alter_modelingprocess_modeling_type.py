# Generated by Django 3.2 on 2021-10-21 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelingprocess',
            name='modeling_type',
            field=models.CharField(default='gensim.models.LdaModel', max_length=250),
        ),
    ]