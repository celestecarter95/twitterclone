# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'pics/%Y/%m/%d', blank=True),
        ),
    ]
