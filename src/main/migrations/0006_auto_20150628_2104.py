# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150628_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='story',
            field=models.ForeignKey(verbose_name='Story', to='main.Story'),
        ),
    ]
