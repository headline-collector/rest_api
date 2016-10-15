# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20161015_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='app_key',
            field=models.CharField(max_length=128, unique=True, null=True, verbose_name=b'app_key', db_column=b'app_key'),
        ),
        migrations.AlterField(
            model_name='app',
            name='token',
            field=models.CharField(max_length=255, unique=True, null=True, verbose_name=b'token'),
        ),
    ]
