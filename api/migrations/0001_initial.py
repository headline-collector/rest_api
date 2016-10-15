# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.IntegerField(verbose_name=b'created_at', null=True, auto_created=True, db_index=True)),
                ('app_key', models.CharField(unique=True, max_length=128, verbose_name=b'app_key', db_column=b'app_key')),
                ('app_name', models.CharField(null=True, db_column=b'appname', max_length=32, unique=True, verbose_name=b'appname', db_index=True)),
                ('auth_type', models.CharField(max_length=32, null=True, verbose_name=b'auth_type')),
                ('app_secret', models.CharField(max_length=255, null=True, verbose_name=b'app_secret')),
                ('callback_url', models.URLField(max_length=255, null=True, verbose_name=b'callback_url')),
                ('is_available', models.NullBooleanField(default=False, verbose_name=b'available', db_column=b'available')),
                ('email', models.EmailField(null=True, db_column=b'contact_email', max_length=64, unique=True, verbose_name=b'contact_email', db_index=True)),
                ('latest_update_time', models.IntegerField(null=True, verbose_name=b'update_time', db_column=b'update_time', db_index=True)),
                ('token', models.CharField(unique=True, max_length=255, verbose_name=b'token')),
                ('expire_date', models.DateField(null=True, verbose_name=b'expire_date', db_column=b'expire_date', db_index=True)),
            ],
            options={
                'db_table': 'auth_app',
            },
        ),
    ]
