# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0005_patientsrec_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientsrec',
            name='Photo',
        ),
    ]
