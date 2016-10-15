# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_party', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='tags',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
