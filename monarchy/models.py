from django.db import models
from django.contrib.auth.models import User
from time import  strftime

# Create your models here.
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=50, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.nama_kategori

class Produk(models.Model):
    KETERANGAN= (
		('T','Tersedia'),
		('K','Kosong')
	)
    kategori=models.ForeignKey(Kategori,null=True)
    nama_produk=models.CharField(max_length=128)
    deskripsi=models.TextField()
    harga=models.IntegerField(max_length=6)
    keterangan=models.CharField(max_length=1,choices=KETERANGAN,null=True,blank=True)
    gambar=models.ImageField(upload_to='static/images/',null=True,blank=True)
	
    def __str__(self):
	return self.nama_produk


class Customer(models.Model):
	JENIS_KELAMIN = (
		('L','Laki-Laki'),
		('P','Perempuan')
	)
	user = models.OneToOneField(User,null=True,blank=True)
	nama_cus = models.CharField(max_length=100,null=True,blank=True)
	jenis_kel=models.CharField(max_length=1,choices=JENIS_KELAMIN,null=True,blank=True)
	no_hp=models.CharField(max_length=12,null=True,blank=True)
	email=models.EmailField(null=True,blank=True)
	def __str__(self):
		return self.nama_cus

class Pesanan(models.Model):
	PENYAJIAN = (
		('TA','take away'),
		('MT','makan di tempat')
	)
	nama_pel = models.ForeignKey(Customer, related_name="user_pesanan")
	nama_produk = models.ForeignKey(Produk, related_name="nama_produk_pesanan")
	jum_pesanan = models.IntegerField(max_length=3)
	penyajian = models.CharField(choices=PENYAJIAN, max_length=3)
	harga = models.IntegerField(max_length=7)
	catatan=models.TextField()
 	def __str__(self):
		return self.nama_pel.nama_cus


class Kasir(models.Model):
	JENIS_KELAMIN = (
		('L','Laki-Laki'),
		('P','Perempuan')
	)
	user = models.OneToOneField(User,null=True,blank=True)
	nama_kasir = models.CharField(max_length=100,null=True,blank=True)
	jenis_kelamin=models.CharField(max_length=1,choices=JENIS_KELAMIN,null=True,blank=True)
	tanggal_lahir=models.DateField(auto_now_add=False,null=True,blank=True)
	no_hp=models.CharField(max_length=12,null=True,blank=True)
	alamat=models.CharField(max_length=50,null=True,blank=True)
	def __str__(self):
		return self.nama_kasir

class DetailTransaksi(models.Model):
	JENIS_PEMBAYARAN = (
		('T','Tunai'),
		('K','Kartu Kredit')
	)
	jenis_transaksi=models.CharField(max_length=1,choices=JENIS_PEMBAYARAN,null=True,blank=True)
	no_faktur=models.CharField(max_length=10,null=True,blank=True)
	tanggal_transaksi=models.DateField(auto_now=True,null=True,blank=True)
	jam_transaksi=models.TimeField(auto_now=True,null=True,blank=True)
	nama_kasir=models.ForeignKey(Kasir,related_name='nama_kasir_transaksi',null=True,blank=True)
	jumlah_bayar=models.IntegerField(null=True,blank=True)
	customer=models.ForeignKey(Customer,null=True,blank=True)
	
	
	def __str__(self):
		jam=str(self.jam_transaksi)
		jam=jam[0:8]
		return ("Transaksi {} pada tanggal {} jam {}").format(self.id,self.tanggal_transaksi,jam)

	
