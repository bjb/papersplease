from django.conf.urls import patterns, url

from .views import upload


urlpatterns = patterns('',
    url(r'^upload/(\w+)/$', upload, name='upload'),
)
