# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gthockey', '0004_team_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='news')),
                ('content', models.CharField(blank=True, max_length=10000)),
            ],
        ),
    ]