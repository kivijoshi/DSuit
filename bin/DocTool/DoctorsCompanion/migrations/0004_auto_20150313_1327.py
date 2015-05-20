# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0003_auto_20150313_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitsrec',
            name='Patient_Visit_Time',
            field=models.TimeField(default=datetime.datetime(2015, 3, 13, 13, 27, 49, 242389, tzinfo=utc), verbose_name=b'Visit Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsrec',
            name='Email',
            field=models.EmailField(max_length=75, verbose_name=b'Email     :', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientsrec',
            name='Occupation',
            field=models.CharField(max_length=50, verbose_name=b'Occupation:', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientsrec',
            name='Reg_Time',
            field=models.TimeField(verbose_name=b'Registration Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitsrec',
            name='Patient_Visit_Date',
            field=models.DateField(verbose_name=b'Visit Date'),
            preserve_default=True,
        ),
    ]
