from django.db import models
from profiles.models import UserProfile


# https://djangocentral.com/building-a-blog-application-with-django/
class BlogPost(models.Model):

    author = models.ForeignKey(UserProfile,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               null=False, blank=True)
    title = models.CharField(max_length=120,
                             null=True, blank=False)
    subtitle = models.CharField(max_length=180,
                                null=True, blank=False)
    content = models.TextField()
    slug = models.SlugField(unique=True,
                            max_length=250, default=None)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)
    title_image = models.ImageField(null=True, blank=True)
    title_image_url = models.URLField(max_length=1024,
                                      null=True, blank=True)

    def __str__(self):
        return self.title
