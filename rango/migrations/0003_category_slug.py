# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150808_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 8, 8, 14, 33, 0, 990189, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
