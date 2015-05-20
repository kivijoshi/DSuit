# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webcam.fields
import webcam.storage


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0008_remove_patientsrec_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsrec',
            name='photo',
            field=webcam.fields.CameraField(storage=webcam.storage.CameraStorage(), upload_to=b'pictures', null=True, verbose_name=b'CameraPictureField', blank=True),
            preserve_default=True,
        ),
    ]
