from django.contrib import admin

from .models import Author, Category, Post, Comment, PostView


# Customize the Admin
admin.site.site_header = 'PiComm Adminstration'
# admin.site.site_title =  'PiComm Adminstration'

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)