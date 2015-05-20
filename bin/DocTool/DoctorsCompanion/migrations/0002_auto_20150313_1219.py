# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsrec',
            name='Reg_Date',
            field=models.TimeField(verbose_name=b'Registration date'),
            preserve_default=True,
        ),
    ]
