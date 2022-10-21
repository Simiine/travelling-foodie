from . import views
from django.urls import path
from .views import ExperienceEditView, ExperienceDeleteView

urlpatterns = [
    path('', views.ExperienceList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('add_experience/', views.add_experience, name='add_experience'),
    path('like/<slug:slug>', views.ExperienceLike.as_view(),
         name='experience_like'),
    path('experience_edit/<slug:slug>', views.ExperienceEditView.as_view(),
         name='experience_edit'),
    path('experience_delete/<slug:slug>', views.ExperienceDeleteView.as_view(),
         name='experience_delete'),
    path('delete_comment/<int:pk>', views.ExperienceDeleteComment.as_view(),
         name='delete_comment'),
    path('<slug:slug>/', views.ExperienceDetail.as_view(),
         name='experience_detail'),
]
