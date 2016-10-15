# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_party', '0003_auto_20161015_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userwebsite',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userwebsite',
            old_name='website_id',
            new_name='website',
        ),
    ]
