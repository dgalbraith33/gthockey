# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gthockey', '0010_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('coach_position', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('image', models.ImageField(upload_to='coach')),
                ('bio', models.CharField(max_length=1000)),
                ('priority', models.IntegerField()),
            ],
        ),
    ]
