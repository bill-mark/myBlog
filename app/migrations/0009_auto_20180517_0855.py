# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-17 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180517_0825'),
        ('app', '0008_remove_light_app_memberlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='light_app',
            name='author_id',
        ),
        migrations.AddField(
            model_name='light_app',
            name='memberlist',
            field=models.ManyToManyField(to='user.User'),
        ),
    ]
