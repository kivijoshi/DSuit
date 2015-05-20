# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webcam.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0006_remove_patientsrec_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsrec',
            name='picture',
            field=webcam.fields.CameraField(default=1),
            preserve_default=False,
        ),
    ]
