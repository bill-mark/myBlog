# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180516_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portal_app',
            name='app_id',
        ),
        migrations.RemoveField(
            model_name='portal_app',
            name='mob_status',
        ),
        migrations.RemoveField(
            model_name='portal_app',
            name='opt_uid',
        ),
        migrations.RemoveField(
            model_name='portal_app',
            name='pc_run_type',
        ),
        migrations.RemoveField(
            model_name='portal_app',
            name='pc_url',
        ),
        migrations.RemoveField(
            model_name='portal_app',
            name='status',
        ),
    ]