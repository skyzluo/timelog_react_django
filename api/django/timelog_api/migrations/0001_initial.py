# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ts', models.DateTimeField()),
                ('text', models.TextField()),
            ],
        ),
    ]
