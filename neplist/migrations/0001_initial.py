# Generated by Django 2.0 on 2018-04-08 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_file', models.FileField(upload_to='check_files')),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CheckListTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('lists', models.ManyToManyField(blank=True, null=True, to='neplist.CheckListTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='CheckTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('lists', models.ManyToManyField(to='neplist.CheckList')),
            ],
        ),
        migrations.CreateModel(
            name='Cron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('minute', models.IntegerField()),
                ('hour', models.IntegerField()),
                ('day_of_month', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day_of_week', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='checklisttemplate',
            name='repeat_rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neplist.Cron'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neplist.CheckListTemplate'),
        ),
        migrations.AddField(
            model_name='check',
            name='checklist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neplist.CheckList'),
        ),
        migrations.AddField(
            model_name='check',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neplist.CheckTemplate'),
        ),
    ]