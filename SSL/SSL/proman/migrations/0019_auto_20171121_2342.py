# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-21 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0018_auto_20171121_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['endYear']},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
