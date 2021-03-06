import json
from datetime import date


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.db.models import Sum
from monarchy.models import *

from .form import *

class InsideView(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(InsideView, self).dispatch(request, *args, **kwargs)


def home(request):
    return render(request,'home-welcome.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
		if request.user.groups.filter(name='admin').exists():
                	return HttpResponseRedirect('/monarchy/all-produk/')
		elif request.user.groups.filter(name='customer').exists():
                	return HttpResponseRedirect('/monarchy/kategori/')
		elif request.user.groups.filter(name='dapur').exists():
                	return HttpResponseRedirect('/monarchy//')
            else:
                #redirect to disable account msg
                messages.error(request,'Akun anda tidak aktif :(')
                return HttpResponseRedirect(reverse('login'))
        else:
            #invalid login
            messages.error(request,'Maaf, username atau password yang anda masukan salah!')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request,'home-welcome.html')


class ProdukInputView(InsideView,View):
    template_name = 'produk/input-produk.html'
    def get(self,request):
        form = ProdukForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = ProdukForm(request.POST or None)
        if form.is_valid():
            input_produk = form.save(commit=False)
            input_produk.save()

            messages.success(request,'Data Produk telah selesai diinput')
            return HttpResponseRedirect(reverse('all-produk'))
        else:
            messages.error(request,'Data tidak lengkap!')
            return render(request,self.template_name,{'form':form})

class ProdukUpdateView(InsideView,UpdateView):

    model = Produk
    template_name = 'produk/update-produk.html'
    form_class = ProdukForm

    def get_success_url(self):
        return reverse('all-produk')

    def get_context_data(self, **kwargs):

        context = super(ProdukUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-produk', kwargs={'pk': self.get_object().id})

        return context

class ProdukDetailView(InsideView,DetailView):
    model = Produk
    template_name = 'produk/detail-produk.html'

class ProdukAllView(InsideView,View):
    template_name = 'produk/all-produk.html'

    def get(self,request):
        produk = Produk.objects.all()

        return render(request,self.template_name,{'produk':produk})

class PesananInputView(InsideView,View):
    template_name = 'pesanan/input-pesanan.html'
    def get(self,request):
        form = PesananForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = PesananForm(request.POST or None)
        if form.is_valid():
            input_pesanan = form.save(commit=False)
            input_pesanan.save()

            messages.success(request,'Data Pesanan telah selesai diinput')
            return HttpResponseRedirect(reverse('kategori'))
        else:
            messages.error(request,'Data tidak lengkap!')
            return render(request,self.template_name,{'form':form})

class PesananAllView(InsideView,View):
    template_name = 'pesanan/all-pesanan.html'

    def get(self,request):
        pesanan = Pesanan.objects.all()

        return render(request,self.template_name,{'pesanan':pesanan})

def kategori_view(request):
    kategori_list=Kategori.objects.all()
    context_dict={"kategori_list":kategori_list}
    return render(request, 'daftarmenu/kategori.html', context_dict)

def menu_view(request,pk):
    kategori = Kategori.objects.get(id=pk)
    menu_list=Produk.objects.filter(kategori=kategori)
    
    context_dict={"menu_list":menu_list}
    try:
	    cust = Customer.objects.get(user=request.user)
	    order = Pesanan.objects.filter(nama_pel=cust)[:-1]
            context_dict['order'] = order 
    except:
            pass
    return render(request, 'menu.html', context_dict)

def pesanan_view(request):
    pesanan_list=Pesanan.object.all()
    context_dict={"pesanan_list":pesanan_list}
    return render(request, 'pesanan.html', context_dict)

