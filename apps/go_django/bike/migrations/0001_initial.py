# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-26 23:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('asset_type', models.CharField(choices=[('P', 'Pump'), ('T', 'Toolkit'), ('V', 'Vest')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=40)),
                ('low_step', models.BooleanField()),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.Bike')),
            ],
        ),
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('operation', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('schedule', models.TextField(default='24 hours every day except holidays')),
            ],
        ),
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=40)),
                ('wi_mm', models.CharField(max_length=40)),
                ('bike', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bike.Bike')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalAsset',
            fields=[
                ('id', models.CharField(db_index=True, max_length=12)),
                ('asset_type', models.CharField(choices=[('P', 'Pump'), ('T', 'Toolkit'), ('V', 'Vest')], max_length=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('fleet', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='bike.Fleet')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical asset',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalBike',
            fields=[
                ('id', models.CharField(db_index=True, max_length=12)),
                ('serial_number', models.CharField(max_length=40)),
                ('low_step', models.BooleanField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('fleet', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='bike.Bike')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical bike',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalGPS',
            fields=[
                ('id', models.CharField(db_index=True, max_length=12)),
                ('serial_number', models.CharField(max_length=40)),
                ('wi_mm', models.CharField(max_length=40)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('bike', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='bike.Bike')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical gps',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalLock',
            fields=[
                ('id', models.CharField(db_index=True, max_length=12)),
                ('serial_number', models.CharField(max_length=40)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('bike', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='bike.Bike')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical lock',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalSteward',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('A', 'The main active bike steward'), ('B', 'A designated back-up steward'), ('I', 'The steward is no longer active')], max_length=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('fleet', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='bike.Fleet')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical steward',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=40)),
                ('bike', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bike.Bike')),
            ],
        ),
        migrations.CreateModel(
            name='Steward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('A', 'The main active bike steward'), ('B', 'A designated back-up steward'), ('I', 'The steward is no longer active')], max_length=1)),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.Fleet')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='fleet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.Fleet'),
        ),
    ]
