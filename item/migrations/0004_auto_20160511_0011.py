# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20160427_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='defaultValue',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
