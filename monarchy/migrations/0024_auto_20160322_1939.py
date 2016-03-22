# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monarchy', '0023_auto_20160322_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='nama_produk',
            field=models.ForeignKey(related_name='nama_produk_pesanan', to='monarchy.Produk'),
            preserve_default=True,
        ),
    ]
