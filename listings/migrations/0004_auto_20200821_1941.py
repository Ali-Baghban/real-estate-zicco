# Generated by Django 3.0.5 on 2020-08-21 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200706_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 21, 19, 41, 48, 518636)),
        ),
    ]
