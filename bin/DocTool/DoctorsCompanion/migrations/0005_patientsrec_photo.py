# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webcam.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0004_auto_20150313_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsrec',
            name='Photo',
            field=webcam.fields.CameraField(null=True, verbose_name=b'CameraPictureField', blank=True),
            preserve_default=True,
        ),
    ]
