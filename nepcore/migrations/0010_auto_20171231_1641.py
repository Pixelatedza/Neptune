# Generated by Django 2.0 on 2017-12-31 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nepcore', '0009_auto_20171231_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nepmenu',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nepmenu',
            name='link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='nepmenu',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menus', related_query_name='menu', to='nepcore.NEPMenu'),
        ),
        migrations.AlterField(
            model_name='nepmenu',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nepmenu',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
