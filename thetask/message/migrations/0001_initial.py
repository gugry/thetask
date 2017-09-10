# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simple_name', models.CharField(max_length=200)),
                ('simple_text', models.CharField(max_length=200)),
                ('simple_number', models.IntegerField(default=0)),
            ],
        ),
    ]
