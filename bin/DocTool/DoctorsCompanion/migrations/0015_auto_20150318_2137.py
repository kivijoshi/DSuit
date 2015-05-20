# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0014_delete_print_cerificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialrecord',
            name='Entry_Date_1',
        ),
        migrations.AddField(
            model_name='financialrecord',
            name='Date',
            field=models.DateField(default=datetime.datetime(2015, 3, 18, 21, 37, 9, 921818), verbose_name=b'Date'),
            preserve_default=True,
        ),
    ]
