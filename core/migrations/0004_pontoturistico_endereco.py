# Generated by Django 3.2.6 on 2021-10-12 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0003_auto_20211011_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ManyToManyField(to='enderecos.Endereco'),
        ),
    ]
