# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-19 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gthockey', '0009_auto_20160430_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='school',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('F', 'F'), ('D', 'D'), ('G', 'G'), ('M', 'M')], default='F', max_length=1),
        ),
    ]
