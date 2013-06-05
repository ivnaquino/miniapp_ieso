from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniapp.views.home', name='home'),
    # url(r'^miniapp/', include('miniapp.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^',include('miniapp.apps.ieso.urls')),

)
