# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
