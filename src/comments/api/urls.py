#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 17/01/2017


from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,
)

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
]

