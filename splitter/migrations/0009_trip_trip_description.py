# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0008_trip_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]