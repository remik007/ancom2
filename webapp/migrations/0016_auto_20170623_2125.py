# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 19:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20170623_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='name',
            new_name='title',
        ),
    ]
