# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 15:43
from __future__ import unicode_literals

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171010_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]
