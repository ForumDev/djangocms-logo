# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=30, null=True, blank=True)),
                ('description', models.TextField(default=b'', max_length=100, null=True, blank=True)),
                ('url', models.URLField(help_text=b'Link to an external page (will override page link)', null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'images/logo/', verbose_name=b'Logo image')),
                ('page', cms.models.fields.PageField(blank=True, to='cms.Page', help_text=b'Select an existing page to link to.', null=True, verbose_name=b'page')),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'Logos',
            },
            bases=(models.Model,),
        ),
    ]
