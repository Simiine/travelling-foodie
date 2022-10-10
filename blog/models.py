from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django_countries.fields import CountryField
from django_summernote.fields import SummernoteTextField
from djangoratings.fields import RatingField

STATUS = ((0, "Draft"), (1, "Published"))



