from django.conf.urls import patterns, include, url
from django.contrib import admin
from monarchy import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),



    url(r'^$', views.home, name='home'),


    url(r'^input-produk/$', views.ProdukInputView.as_view(),name='input-produk'),

    url(r'^edit-produk/(?P<pk>\d+)/$', views.ProdukUpdateView.as_view(),name='edit-produk'),

    url(r'^detail-produk/(?P<pk>\d+)/$', views.ProdukDetailView.as_view(),name='detail-produk',),

    url(r'^all-produk/$', views.ProdukAllView.as_view(),name='all-produk'),
    url(r'^kategori/$', views.kategori_view, name='kategori'),  
    url(r'^menu/(?P<pk>\d+)/$', views.menu_view, name='menu'),
    url(r'^input-pesanan/$', views.PesananInputView.as_view(), name='input-pesanan'),
    url(r'^all-pesanan/$', views.PesananAllView.as_view(), name='all-pesanan'),
    
)
