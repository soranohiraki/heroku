# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-02 15:43
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import splitter.models


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0035_auto_20170707_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='itinerary',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=splitter.models.itinerary_json_default),
        ),
    ]
