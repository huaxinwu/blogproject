#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Post,Tag,Category
# 定制admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)