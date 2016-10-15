# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20161015_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='user_name',
        ),
        migrations.AddField(
            model_name='app',
            name='username',
            field=models.CharField(db_column=b'username', default='', max_length=64, unique=True, verbose_name=b'username', db_index=True),
            preserve_default=False,
        ),
    ]
