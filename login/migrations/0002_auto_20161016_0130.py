# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todolist',
            name='activity',
            field=models.CharField(max_length=256),
        ),
    ]
