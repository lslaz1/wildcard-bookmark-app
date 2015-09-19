"""wildcard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bookmark_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^bookmarks$', views.bookmarks, name='bookmarks'),
    url(r'^bookmark/new$', views.new, name='new'),
    url(r'^bookmark/create$', views.create, name='create'),
    url(r'^bookmark/(?P<bm_id>\d+)/update$', views.update, name='update'),
    url(r'^bookmark/(?P<bm_id>\d+)/update_url$', views.update_url, name='udpate_url'),
    url(r'^bookmark/(?P<bm_id>\d+)/update_desc$', views.update_desc, name='update_desc'),
    url(r'^bookmark/(?P<bm_id>\d+)/remove$', views.remove, name='remove'),

]	
