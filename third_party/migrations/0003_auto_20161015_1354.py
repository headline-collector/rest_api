# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('third_party', '0002_website_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_id',
            field=models.ForeignKey(related_name='App.id+', db_column=b'auth_id', verbose_name=b'auth', to=settings.AUTH_USER_MODEL),
        ),
    ]
