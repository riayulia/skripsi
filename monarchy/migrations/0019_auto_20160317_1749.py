# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monarchy', '0018_auto_20160315_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kode_produk', models.CharField(max_length=2)),
                ('kategori', models.CharField(max_length=10)),
                ('nama_produk', models.CharField(max_length=20)),
                ('deskripsi', models.CharField(max_length=40)),
                ('harga', models.IntegerField(max_length=6)),
                ('keterangan', models.CharField(max_length=8)),
                ('gambar', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProdukTransaksi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jumlah_produk', models.IntegerField(null=True, blank=True)),
                ('total_harga', models.IntegerField(null=True, blank=True)),
                ('detail', models.ForeignKey(related_name='detail-transaksi', blank=True, to='monarchy.DetailTransaksi', null=True)),
                ('produk', models.ForeignKey(related_name='produk_yang_diulang', blank=True, to='monarchy.Produk', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='barang',
            name='perusahaan',
        ),
        migrations.RemoveField(
            model_name='barangtransaksi',
            name='barang',
        ),
        migrations.RemoveField(
            model_name='barangtransaksi',
            name='detail',
        ),
        migrations.DeleteModel(
            name='BarangTransaksi',
        ),
        migrations.DeleteModel(
            name='Perusahaan',
        ),
        migrations.RemoveField(
            model_name='stok',
            name='nama_barang',
        ),
        migrations.DeleteModel(
            name='Stok',
        ),
        migrations.RemoveField(
            model_name='diskon',
            name='nama_barang',
        ),
        migrations.DeleteModel(
            name='Barang',
        ),
        migrations.AddField(
            model_name='diskon',
            name='nama_produk',
            field=models.ForeignKey(related_name='produk_diskon', blank=True, to='monarchy.Produk', null=True),
            preserve_default=True,
        ),
    ]
