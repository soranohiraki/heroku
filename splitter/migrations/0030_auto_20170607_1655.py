# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0029_auto_20170607_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]