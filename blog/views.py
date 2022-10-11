from django.shortcuts import render
from django.views import generic
from .models import Experience

class ExperienceList(generic.ListView):
    """
    Creates Experience list
    """
    model = Experience
    queryset = Experience.objects.filter(status=1).order_by('-created_on')
    