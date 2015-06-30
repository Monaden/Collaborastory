# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150624_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='story',
            field=models.ForeignKey(default='', verbose_name='Story', to='main.Story'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='uuid',
            field=models.CharField(max_length=64, default=''),
        ),
    ]
