# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactUs',
            new_name='ContactUsForm',
        ),
    ]
