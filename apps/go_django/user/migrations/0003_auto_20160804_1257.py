# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20160804_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='id',
            field=models.CharField(max_length=80, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historicalenduser',
            name='id',
            field=models.CharField(db_index=True, max_length=80),
        ),
    ]
