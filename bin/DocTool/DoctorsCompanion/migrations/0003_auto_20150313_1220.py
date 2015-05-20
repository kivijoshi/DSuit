# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0002_auto_20150313_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsrec',
            name='Reg_Time',
            field=models.TimeField(default=datetime.datetime(2015, 3, 13, 12, 20, 52, 864615, tzinfo=utc), verbose_name=b'Registration date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsrec',
            name='Reg_Date',
            field=models.DateField(verbose_name=b'Registration date'),
            preserve_default=True,
        ),
    ]
