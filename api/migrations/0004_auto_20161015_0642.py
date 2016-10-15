# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_app_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='email',
            field=models.EmailField(null=True, db_column=b'contact_email', default=b'', max_length=64, unique=True, verbose_name=b'contact_email', db_index=True),
        ),
    ]
