# Generated by Django 3.0.5 on 2020-08-21 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_name', models.CharField(max_length=50, null=True)),
                ('listing_id', models.IntegerField()),
                ('client_email', models.CharField(max_length=40, null=True)),
                ('client_name', models.CharField(max_length=50, null=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('checking', models.BooleanField(default=False)),
            ],
        ),
    ]