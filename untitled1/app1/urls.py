# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app1 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url for rendering pages
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_info/$', views.add_info, name='add_info'),
    url(r'^add_showcase/$', views.add_showcase, name='add_showcase'),
    url(r'^add_note/$', views.add_note, name='add_note'),
    url(r'^stage/$', views.stage, name='stage'),
    url(r'^background/$', views.background, name='background'),

    # url interface
    # url(r'^api_register/$', views.api_register, name='api_register'),
    # url(r'^api_add_info/$', views.api_add_info, name='api_add_info'),
    # url(r'^api_add_showcase/$', views.api_add_showcase, name='api_add_showcase'),
    # url(r'^api_add_note/$', views.api_add_note, name='api_add_note'),

    url(r'^api_latest_job/$', views.api_latest_job, name='api_latest_job'),
    url(r'^api_latest_note/$', views.api_latest_note, name='api_latest_note'),
    url(r'^api_info/$', views.api_info, name='api_info'),
    url(r'^api_showcase/$', views.api_showcase, name='api_showcase'),
    url(r'^api_note/$', views.api_note, name='api_note'),
    url(r'^api_job/$', views.api_job, name='api_job'),
)
