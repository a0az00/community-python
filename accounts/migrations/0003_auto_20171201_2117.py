# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171201_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(blank=True, null=True, verbose_name='自我介绍'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='电话'),
        ),
    ]
