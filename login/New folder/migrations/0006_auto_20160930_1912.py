# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='users',
            name='confirm_password',
            field=models.CharField(max_length=256, null=True),
        ),
    ]