# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 20:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('topic', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
