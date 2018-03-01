# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('time', models.TimeField(null=True, blank=True)),
                ('venue', models.CharField(default='H', max_length=1, choices=[('H', 'Home'), ('A', 'Away'), ('T', 'Tournament')])),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('position', models.CharField(default='F', max_length=1, choices=[('F', 'F'), ('D', 'D'), ('G', 'G')])),
                ('number', models.IntegerField(null=True, blank=True)),
                ('hometown', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('rink_name', models.CharField(max_length=50)),
                ('maps_url', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('school_name', models.CharField(max_length=50)),
                ('mascot_name', models.CharField(max_length=50, blank=True)),
                ('web_url', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.ForeignKey(null=True, to='gthockey.Rink', on_delete=models.SET_NULL),
        ),
        migrations.AddField(
            model_name='game',
            name='opponent',
            field=models.ForeignKey(null=True, to='gthockey.Team', on_delete=models.SET_NULL),
        ),
    ]
