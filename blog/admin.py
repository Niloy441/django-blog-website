from django.contrib import admin
from .models import Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'updated_date')
    list_filter = ('author', 'created_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_date'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date')
    list_filter = ('post', 'author', 'created_date')
    search_fields = ('text',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_date')
    list_filter = ('post', 'user', 'created_date')