# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-09-23 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('install', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='install_list',
            name='status',
            field=models.CharField(choices=[(0, '未安装'), (1, '已安装')], default=0, max_length=5, verbose_name='安装状态'),
        ),
    ]