# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0002_auto_20151016_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_picture',
            new_name='picture',
        ),
    ]
