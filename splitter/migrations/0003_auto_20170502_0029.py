# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0002_auto_20170502_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
