# Generated by Django 3.1.7 on 2021-02-28 18:44

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('ID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=25)),
                ('Colore', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('Descrizione', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Titolo', models.CharField(max_length=100)),
                ('Testo', models.TextField()),
                ('autore', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autore articolo')),
                ('categoria', models.ForeignKey(blank=True, default='GLD', on_delete=django.db.models.deletion.CASCADE, to='gestione_articoli.categoria', verbose_name='Categoria articolo')),
            ],
            options={
                'verbose_name': 'Articolo',
                'verbose_name_plural': 'Articoli',
            },
        ),
    ]