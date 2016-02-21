# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailrecord',
            name='unsubscribe_guid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
