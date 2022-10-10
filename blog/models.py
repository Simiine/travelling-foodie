from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django_countries.fields import CountryField
from django_summernote.fields import SummernoteTextField
from djangoratings.fields import RatingField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Model for Experiences
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    country = CountryField()
    content = SummernoteTextField()
    recipe = SummernoteTextField()
    rating = RatingField(range=5) # 5 possible rating values, 1-5
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='experience_likes', blank=True)

    class Meta:
        """
        Ordering Experiences
        """
        ordering = ['-created_on']

    
