# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-10 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180109_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='list_image',
            new_name='image',
        ),
    ]
