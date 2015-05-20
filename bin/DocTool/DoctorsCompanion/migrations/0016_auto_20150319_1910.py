# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorsCompanion', '0015_auto_20150318_2137'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrintYourFinances',
        ),
        migrations.AlterField(
            model_name='financialrecord',
            name='Date',
            field=models.DateField(default=datetime.datetime(2015, 3, 19, 19, 10, 53, 493884), verbose_name=b'Date'),
            preserve_default=True,
        ),
    ]
