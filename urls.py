from django.conf.urls.defaults import patterns, include, url
from os.path import dirname, join
from samples.views import main, sample

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

site_media = join(dirname(__file__), 'site_media')
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CalcWorks.views.home', name='home'),
    # url(r'^CalcWorks/', include('CalcWorks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^$', main),
    #(r'^sample/([^\s]+)/$', sample),
    url(r'^$', 'views.home', name='home'),
    url(r'^about/$', 'views.about', name='about'),
    url(r'^contact/$', 'views.contact', name='contact'),
    url(r'^blog/', include('django_yaba.urls')),
    url(r'^work/', include('work.urls')),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    #url(r'^/', include('CalcWorks.foo.urls')),
    #url(r'^([^\s]*)/?$', include('django_yaba.urls')),
    # zinnia
#    url(r'^weblog/', include('zinnia.urls')),
#    url(r'^comments/', include('django.contrib.comments.urls')),
)
