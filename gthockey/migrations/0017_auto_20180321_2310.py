# Generated by Django 2.0.2 on 2018-03-22 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gthockey', '0016_shopitem_shopitemimage_shopitemoptionlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopItemCustomOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=25)),
                ('help_text', models.CharField(blank=True, max_length=50)),
                ('required', models.BooleanField(default=False)),
                ('extra_cost', models.FloatField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='shopitemoptionlist',
            name='help_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='shopitemcustomoption',
            name='shop_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_options', to='gthockey.ShopItem'),
        ),
    ]
