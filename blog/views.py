from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Experience

class ExperienceList(generic.ListView):
    """
    Creates Experience list
    """
    model = Experience
    queryset = Experience.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6