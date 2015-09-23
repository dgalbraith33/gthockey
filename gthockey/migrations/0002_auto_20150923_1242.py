# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gthockey', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['-date', '-time']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['school_name']},
        ),
        migrations.AlterField(
            model_name='game',
            name='location',
            field=models.ForeignKey(null=True, to='gthockey.Rink', blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='opponent',
            field=models.ForeignKey(null=True, to='gthockey.Team', blank=True),
        ),
    ]
