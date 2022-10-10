from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager

STATUS = ((0, "Draft"), (1, "Published"))


