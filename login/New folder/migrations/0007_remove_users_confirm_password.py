# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20160930_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='confirm_password',
        ),
    ]
