# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authorID', models.CharField(unique=True, max_length=255)),
                ('gender', models.CharField(max_length=7)),
                ('age', models.PositiveSmallIntegerField()),
                ('predictedGender', models.CharField(max_length=7)),
                ('predictedAge', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(verbose_name=b'Date requested')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
