from django.shortcuts import render
from django.views import generic
from .models import Experience

class ExperienceList(generic.ListView):
    """
    Creates Experience list
    """
    