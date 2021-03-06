# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-21 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0017_auto_20171117_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrip', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Deg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='completedstudent',
            name='degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proman.Deg'),
        ),
        migrations.AlterField(
            model_name='continuingstudent',
            name='degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proman.Deg'),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
