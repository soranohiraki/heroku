# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 00:08
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0022_auto_20170525_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charge_detail',
            name='charge',
        ),
        migrations.RemoveField(
            model_name='charge_detail',
            name='traveler',
        ),
        migrations.RemoveField(
            model_name='segment_detail',
            name='segment',
        ),
        migrations.AddField(
            model_name='charge',
            name='charge_detail',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='segment_detail',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Charge_Detail',
        ),
        migrations.DeleteModel(
            name='Segment_Detail',
        ),
    ]
