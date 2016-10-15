# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=256)),
                ('post_date', models.DateField(null=True)),
                ('digest', models.CharField(max_length=256, null=True)),
                ('title', models.CharField(unique=True, max_length=64)),
                ('score', models.IntegerField()),
            ],
            options={
                'db_table': 'headline',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=64)),
                ('auth_id', models.OneToOneField(related_name='App.id+', db_column=b'auth_id', verbose_name=b'auth', to='api.App')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserWebSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('importance', models.IntegerField(null=True)),
                ('user_id', models.ForeignKey(to='third_party.User')),
            ],
        ),
        migrations.CreateModel(
            name='WebSite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=256)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'db_table': 'website',
            },
        ),
        migrations.AddField(
            model_name='userwebsite',
            name='website_id',
            field=models.ForeignKey(to='third_party.WebSite'),
        ),
        migrations.AddField(
            model_name='headline',
            name='website_id',
            field=models.ForeignKey(to='third_party.WebSite', db_column=b'website_id'),
        ),
    ]
