# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_party', '0004_auto_20161015_1410'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userwebsite',
            table='user_website',
        ),
    ]
