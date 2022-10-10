from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django_countries.fields import CountryField
from django_summernote.fields import SummernoteTextField
from djangoratings.fields import RatingField

STATUS = ((0, "Draft"), (1, "Published"))

class Experience(models.Model):
    """
    Model for Experiences
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experience")
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
        Ordering Experiences in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        Returns the number of likes on an experience
        """
        return self.likes.count()

class Comment(models.Model):
    """
    Model for comment
    """
    experience = models.ForeignKey(experience, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

