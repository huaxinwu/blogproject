#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
# Create your views here.
app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]