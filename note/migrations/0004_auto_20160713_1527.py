# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20160712_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='end_time',
            field=models.DateTimeField(),
        ),
    ]
