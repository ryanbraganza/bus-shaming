# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-15 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busshaming', '0021_trip_scheduled'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='realtimeprogress',
            unique_together=set([('feed', 'start_date')]),
        ),
    ]
