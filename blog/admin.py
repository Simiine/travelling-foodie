from django.contrib import admin
from .models import Experience
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Experience)
class ExperienceAdmin(SummernoteModelAdmin):

    summernote_fields = ('content', 'recipe')


