# Generated by Django 3.2.6 on 2021-10-12 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0004_pontoturistico_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='endereco',
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
        ),
    ]