from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django_countries.fields import CountryField
from django.template.defaultfilters import slugify

#from django_summernote.fields import SummernoteTextField 

STATUS = ((0, "Draft"), (1, "Published"))

class Experience(models.Model):
    """
    Model for Experiences
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experiences")
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    country = CountryField()
    content = models.TextField() #SummernoteTextField()
    recipe = models.TextField() #SummernoteTextField()
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    """
    Model for comment
    """
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order comments in ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Return string representation
        """
        return f"Comment {self.body} by {self.author}"

