# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogger_gender_and_age', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='predictedAge',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='predictedGender',
            field=models.CharField(max_length=7, null=True),
            preserve_default=True,
        ),
    ]
