from django import forms
from .models import Experience, Comment
from django.contrib.auth.forms import UserCreationForm

class CommentForm(forms.ModelForm):
    """
    Form for Comments
    """
    class Meta:
        model = Comment
        fields = ('body',)

class ExperienceForm(forms.ModelForm):
    """
    Form to Add Experience
    """
    class Meta:
        model = Experience
        fields = ('slug', 'title', 'featured_image', 'country', 'content', 'recipe', 'tags',)
    
    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)