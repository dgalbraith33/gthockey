# Generated by Django 2.0.2 on 2018-06-07 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gthockey', '0017_auto_20180321_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitem',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shopitem',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
