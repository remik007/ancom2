# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0030_slider_image_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='image_thumbnail',
        ),
    ]