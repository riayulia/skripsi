# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monarchy', '0022_auto_20160320_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='nama_kategori',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar',
            field=models.ImageField(null=True, upload_to=b'static/images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produk',
            name='kategori',
            field=models.ForeignKey(to='monarchy.Kategori', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produk',
            name='keterangan',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'T', b'Tersedia'), (b'K', b'Kosong')]),
            preserve_default=True,
        ),
    ]
