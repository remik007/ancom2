# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='first',
            field=models.BooleanField(default=False),
        ),
    ]
