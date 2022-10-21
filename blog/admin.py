from django.contrib import admin
from .models import Experience, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Experience)
class ExperienceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on', 'country') #'tags')
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on') #'tags')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'recipe')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'experience', 'created_on', 'approved')
    list_filter = ('author', 'created_on', 'approved')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
