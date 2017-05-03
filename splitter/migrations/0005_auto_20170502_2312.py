# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 03:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('splitter', '0004_auto_20170502_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='charge_detail',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='users',
        ),
        migrations.AddField(
            model_name='charge_detail',
            name='traveler',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='splitter.Traveler'),
        ),
        migrations.AddField(
            model_name='trip',
            name='travelers',
            field=models.ManyToManyField(to='splitter.Traveler'),
        ),
    ]
