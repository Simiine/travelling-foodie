from django.contrib import admin
from .models import Experience
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Experience)
class ExperienceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on', 'country', 'tags')
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'recipe')


