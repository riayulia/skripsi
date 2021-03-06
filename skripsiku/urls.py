from django.conf.urls import patterns, include, url
from django.contrib import admin
from monarchy import urls_monarchy
from monarchy import views
from django.http import HttpResponseRedirect


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skripsiku.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^monarchy/',include(urls_monarchy)),

)
