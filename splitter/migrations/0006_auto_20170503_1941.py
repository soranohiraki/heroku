# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0005_auto_20170502_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='output_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
