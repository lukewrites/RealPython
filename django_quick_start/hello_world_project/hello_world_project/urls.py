from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('hello_world.urls')),
                       url(r'^help/', include('hello_world.urls')),
                       url(r'^about/', include('hello_world.urls')),
)
