# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-17 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0016_auto_20171116_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='description',
            new_name='descrip',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='description',
            new_name='descrip',
        ),
    ]