# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20160427_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='dataType',
            field=models.CharField(choices=[(b'str', b'String'), (b'int', b'Integer'), (b'dat', b'Date'), (b'tim', b'Time')], default=b'str', max_length=50),
        ),
    ]
