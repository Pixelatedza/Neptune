# Generated by Django 2.0 on 2017-12-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nepcore', '0006_nepsiteconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='nepsiteconfig',
            name='default_view',
            field=models.CharField(default='index', max_length=255),
        ),
    ]