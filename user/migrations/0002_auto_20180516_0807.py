# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='app_list',
            field=models.CharField(max_length=100, null=True),
        ),
    ]