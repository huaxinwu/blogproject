#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
from django import template
from ..models import Post,Category,Tag
from django.db.models.aggregates import Count

# 实例化了一个 template.Library 类
register = template.Library()
# 定义函数--最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
# 定义函数--归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')
# 定义函数--分类模板标签
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    #return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

# 定义函数--标签云标签
@register.simple_tag
def get_tagcloud():
    #return Tag.objects.all()
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)