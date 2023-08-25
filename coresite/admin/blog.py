from django.contrib import admin
from coresite.models.blog import Blog

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'title')