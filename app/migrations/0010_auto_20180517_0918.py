# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-17 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180517_0825'),
        ('app', '0009_auto_20180517_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='light_app',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_lightapps_author', to='user.User'),
        ),
        migrations.AlterField(
            model_name='light_app',
            name='memberlist',
            field=models.ManyToManyField(related_name='user_lightapps_member', to='user.User'),
        ),
    ]
