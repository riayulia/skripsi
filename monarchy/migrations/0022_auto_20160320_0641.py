# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monarchy', '0021_remove_produk_kode_produk'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailTransaksi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jenis_transaksi', models.CharField(blank=True, max_length=1, null=True, choices=[(b'T', b'Tunai'), (b'K', b'Kartu Kredit')])),
                ('no_faktur', models.CharField(max_length=10, null=True, blank=True)),
                ('tanggal_transaksi', models.DateField(auto_now=True, null=True)),
                ('jam_transaksi', models.TimeField(auto_now=True, null=True)),
                ('jumlah_bayar', models.IntegerField(null=True, blank=True)),
                ('customer', models.ForeignKey(blank=True, to='monarchy.Customer', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kasir',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_kasir', models.CharField(max_length=100, null=True, blank=True)),
                ('jenis_kelamin', models.CharField(blank=True, max_length=1, null=True, choices=[(b'L', b'Laki-Laki'), (b'P', b'Perempuan')])),
                ('tanggal_lahir', models.DateField(null=True, blank=True)),
                ('no_hp', models.CharField(max_length=12, null=True, blank=True)),
                ('alamat', models.CharField(max_length=50, null=True, blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_kategori', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jum_pesanan', models.IntegerField(max_length=3)),
                ('penyajian', models.CharField(max_length=3, choices=[(b'TA', b'take away'), (b'MT', b'makan di tempat')])),
                ('harga', models.IntegerField(max_length=7)),
                ('catatan', models.TextField()),
                ('nama_pel', models.ForeignKey(related_name='user_pesanan', to='monarchy.Customer')),
                ('nama_produk', models.ManyToManyField(related_name='nama_produk_pesanan', to='monarchy.Produk')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='nama_kasir',
            field=models.ForeignKey(related_name='nama_kasir_transaksi', blank=True, to='monarchy.Kasir', null=True),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='jenis_kelamin',
            new_name='jenis_kel',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='nama',
            new_name='nama_cus',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='alamat',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='kode_pos',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='kota',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='tanggal_lahir',
        ),
        migrations.AlterField(
            model_name='produk',
            name='deskripsi',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produk',
            name='kategori',
            field=models.ForeignKey(to='monarchy.Kategori'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produk',
            name='nama_produk',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
