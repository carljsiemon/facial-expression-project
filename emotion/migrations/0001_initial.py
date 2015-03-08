# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import emotion.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificationRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('type', models.PositiveIntegerField(help_text=b'0 for video, 1 for image,                                                 any other undefined', validators=[emotion.models.validate_request_type])),
                ('rand_string', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageClassification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gray_image', models.ImageField(upload_to=emotion.models.gray_scale_file)),
                ('image', models.ImageField(upload_to=emotion.models.original_image_file)),
                ('image_rank', models.IntegerField()),
                ('rank1', models.PositiveIntegerField()),
                ('rank1_prob', models.FloatField(default=0.0)),
                ('rank2', models.PositiveIntegerField()),
                ('rank2_prob', models.FloatField(default=0.0)),
                ('rank3', models.PositiveIntegerField()),
                ('rank3_prob', models.FloatField(default=0.0)),
                ('rank4', models.PositiveIntegerField()),
                ('rank4_prob', models.FloatField(default=0.0)),
                ('rank5', models.PositiveIntegerField()),
                ('rank5_prob', models.FloatField(default=0.0)),
                ('rank6', models.PositiveIntegerField()),
                ('rank6_prob', models.FloatField(default=0.0)),
                ('rank7', models.PositiveIntegerField()),
                ('rank7_prob', models.FloatField(default=0.0)),
                ('request', models.ForeignKey(to='emotion.ClassificationRequest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
