# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_delete_simplemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='message_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]