# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_app_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='user_name',
            field=models.CharField(db_column=b'user_name', default='', max_length=64, unique=True, verbose_name=b'user_name', db_index=True),
            preserve_default=False,
        ),
    ]
