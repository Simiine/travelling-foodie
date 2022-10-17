from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Experience
from .forms import CommentForm

class ExperienceList(generic.ListView):
    """
    Creates Experience list
    """
    model = Experience
    queryset = Experience.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class ExperienceDetail(View):
    """
    Creates Experience detail view
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Experience.objects.filter(status=1)
        experience = get_object_or_404(queryset, slug=slug)
        comments = experience.comments.filter(approved=True).order_by('created_on')
        liked = False
        if experience.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "experience_detail.html",
            {
                "experience": experience,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
