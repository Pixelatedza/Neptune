# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nepcore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nepuser',
            name='nepPermissions',
            field=models.ManyToManyField(blank=True, null=True, to='nepcore.NEPPermission'),
        ),
    ]
