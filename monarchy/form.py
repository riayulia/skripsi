from django import forms



from .models import *
from . import widgets


class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        widgets = {
            'kategori':forms.Select(attrs={'class':'form-control'}),
            'nama_produk':forms.TextInput(attrs={'class':'form-control'}),
            'deskripsi':forms.TextInput(attrs={'class':'form-control'}),
            'harga':forms.TextInput(attrs={'class':'form-control'}),
            'keterangan':forms.Select(attrs={'class':'form-control'}),
            'gambar': widgets.NotClearableFileInput,
        }

class PesananForm(forms.ModelForm):
    class Meta:
        model = Pesanan
        widgets = {
            'nama_pel':forms.Select(attrs={'class':'form-control'}),
            'nama_produk':forms.Select(attrs={'class':'form-control'}),
            'jum_pesanan':forms.TextInput(attrs={'class':'form-control'}),
            'penyajian':forms.Select(attrs={'class':'form-control'}),
            'harga':forms.TextInput(attrs={'class':'form-control'}),
            'catatan':forms.TextInput(attrs={'class':'form-control'}),
        }
