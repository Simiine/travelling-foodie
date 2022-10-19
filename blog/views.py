from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Experience, Comment
from .import forms
from .forms import CommentForm
from .forms import ExperienceForm

class ExperienceList(generic.ListView):
    """
    Creates Experience list
    """
    model = Experience
    queryset = Experience.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Experience.objects.filter(status=1)
        experience = get_object_or_404(queryset, slug=slug)
        comments = experience.comments.filter(approved=True).order_by('created_on')
        liked = False
        if experience.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.experience = experience
            comment.author = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "experience_detail.html",
            {
                "experience": experience,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class ExperienceLike(View):
    """
    Creates experience likes view
    """

    def post(self, request, slug, *args, **kwargs):
        experience = get_object_or_404(Experience, slug=slug)
        if experience.likes.filter(id=request.user.id).exists():
            experience.likes.remove(request.user)
        else:
            experience.likes.add(request.user)
        return HttpResponseRedirect(reverse('experience_detail', args=[slug]))

# @login_required
def add_experience(request):
    """
    Add experience
    """
    experience_form = ExperienceForm()
    print(request.method)
    if request.method == "POST":
        experience_form = ExperienceForm(request.POST, request.FILES)
        print(experience_form.is_valid())
        if experience_form.is_valid():
            experience_form = experience_form.save(commit=False)
            experience_form.title = experience_form.title.title()
            experience_form.author = request.user
            experience_form.status = 1
            experience_form.save()
            return redirect('home')

    return render(request, 'add_experience.html', context={'experience_form': experience_form})

# class ExperienceCreate(CreateView):
#     """ 
#     Create an Experience
#     """
#     model = Experience
#     form_class = ExperienceForm
#     template_name = 'add_experience.html'
#     success_url = reverse_lazy('experience')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

class ExperienceEditView(UpdateView):
    """
    Edit Experience
    """
    model = Experience
    form_class = ExperienceForm
    template_name_suffix = '_edit'
    template_name = 'experience_edit.html'
    # template_name = 'experience_update_form.html'
    success_url = '/'

class ExperienceDeleteView(DeleteView):
    """
    Delete Experience
    """
    model = Experience
    template_name = 'experience_delete.html'
    success_url = reverse_lazy('home')

class ExperienceDeleteComment(DeleteView):
    """
    Delete comment
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')
