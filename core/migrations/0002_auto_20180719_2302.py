# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-19 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='sleep_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='wake_up_time',
            field=models.IntegerField(),
        ),
    ]