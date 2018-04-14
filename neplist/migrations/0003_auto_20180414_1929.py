# Generated by Django 2.0 on 2018-04-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neplist', '0002_auto_20180408_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Fine'), (2, 'Problem'), (3, 'Follow Up')], null=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='proof_file',
            field=models.FileField(blank=True, null=True, upload_to='check_files'),
        ),
    ]