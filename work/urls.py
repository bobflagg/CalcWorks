from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('work.views',
    url(r'^$', 'sample_list', name="work-home"),
    url(r'^(?P<slug>[-\w]+)/$', 'sample_detail', name="work-sample"),
)
