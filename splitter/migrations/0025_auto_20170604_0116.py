# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-04 05:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0024_auto_20170530_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
