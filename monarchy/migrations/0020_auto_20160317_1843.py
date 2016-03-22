# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monarchy', '0019_auto_20160317_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailtransaksi',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='detailtransaksi',
            name='nama_kasir',
        ),
        migrations.RemoveField(
            model_name='diskon',
            name='nama_produk',
        ),
        migrations.DeleteModel(
            name='Diskon',
        ),
        migrations.RemoveField(
            model_name='kasir',
            name='user',
        ),
        migrations.DeleteModel(
            name='Kasir',
        ),
        migrations.RemoveField(
            model_name='produktransaksi',
            name='detail',
        ),
        migrations.DeleteModel(
            name='DetailTransaksi',
        ),
        migrations.RemoveField(
            model_name='produktransaksi',
            name='produk',
        ),
        migrations.DeleteModel(
            name='ProdukTransaksi',
        ),
    ]
