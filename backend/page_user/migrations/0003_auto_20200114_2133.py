# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-14 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_user', '0002_auto_20200114_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersecond',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
