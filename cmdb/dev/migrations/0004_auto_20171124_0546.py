# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0003_auto_20171124_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dev_script',
            name='parameter_num',
            field=models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default='0', max_length=2, verbose_name='参数个数'),
        ),
    ]
