# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 01:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161224_0111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='amazon',
            new_name='wishlist',
        ),
    ]