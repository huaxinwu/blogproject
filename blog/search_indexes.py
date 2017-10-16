#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
from haystack import indexes
from .models import Post

# 使用那些数据建立索引
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()