# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-25 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=20)),
                ('mentor', models.CharField(max_length=20)),
                ('mem1', models.CharField(max_length=20)),
                ('mem2', models.CharField(max_length=20)),
                ('mem3', models.CharField(max_length=20)),
                ('member_nos', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
