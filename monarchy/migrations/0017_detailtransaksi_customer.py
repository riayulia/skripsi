# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monarchy', '0016_remove_detailtransaksi_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailtransaksi',
            name='customer',
            field=models.ForeignKey(blank=True, to='monarchy.Customer', null=True),
            preserve_default=True,
        ),
    ]
