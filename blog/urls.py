from . import views
from django.urls import path

urlpatterns = [
    path('', views.ExperienceList.as_view(), name='home'),
    path('<slug:slug>/', views.ExperienceDetail.as_view(), name='experience_detail'),
]