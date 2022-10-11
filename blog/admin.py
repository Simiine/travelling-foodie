from django.contrib import admin
from .models import Experience
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Experience)
class ExperienceAdmin(SummernoteModelAdmin):
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on', 'tags', 'country')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'recipe')


