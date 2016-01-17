# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'app.views',

    # Examples:
    # url(r'^$', 'lx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/$', 'list'),
    url(r'^$', 'index'),
    url(r'^blogcontent', 'blogcontent'),
)
