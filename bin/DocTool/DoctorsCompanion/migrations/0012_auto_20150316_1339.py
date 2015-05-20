# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webcam.fields
import webcam.storage


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0011_auto_20150316_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsrec',
            name='photo',
            field=webcam.fields.CameraField(default=b'PICTURE_ROOT/profile-default.jpg', storage=webcam.storage.CameraStorage(), upload_to=b'pictures', blank=True, null=True, verbose_name=b'CameraPictureField'),
            preserve_default=True,
        ),
    ]
