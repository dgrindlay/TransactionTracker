# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-14 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='details',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='section',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
