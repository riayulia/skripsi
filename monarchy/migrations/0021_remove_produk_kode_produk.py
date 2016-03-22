# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monarchy', '0020_auto_20160317_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='kode_produk',
        ),
    ]
