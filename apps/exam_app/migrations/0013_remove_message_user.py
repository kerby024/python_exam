# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0012_message_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]
