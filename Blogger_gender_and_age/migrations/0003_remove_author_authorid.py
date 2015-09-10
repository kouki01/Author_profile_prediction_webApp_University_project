# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogger_gender_and_age', '0002_auto_20141207_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='authorID',
        ),
    ]
