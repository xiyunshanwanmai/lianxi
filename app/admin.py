# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from app.models import Author, Blog, Tag

class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email')
    search_fields = ('name',)


class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'id', 'author', 'publish_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)