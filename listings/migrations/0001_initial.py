# Generated by Django 3.0.5 on 2020-05-11 20:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('address', models.TextField()),
                ('bathroom', models.IntegerField(default=1)),
                ('bedroom', models.IntegerField(default=1)),
                ('infr', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 12, 1, 15, 35, 914747))),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]