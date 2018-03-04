# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-01 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gthockey', '0012_merge_20170918_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gthockey.Rink'),
        ),
        migrations.AlterField(
            model_name='game',
            name='opponent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gthockey.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gthockey.Season'),
        ),
    ]