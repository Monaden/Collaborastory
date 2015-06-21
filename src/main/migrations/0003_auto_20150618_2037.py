# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import uuid
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150618_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='owner',
        ),
        migrations.AddField(
            model_name='authors',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='authors',
            name='uuid',
            field=models.CharField(max_length=64, default=uuid.uuid1),
        ),
        migrations.AddField(
            model_name='story',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Time', default=datetime.datetime(2015, 6, 18, 18, 37, 21, 598057, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='score',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='word',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='Time', default=datetime.datetime(2015, 6, 18, 18, 37, 35, 742866, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='word',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
