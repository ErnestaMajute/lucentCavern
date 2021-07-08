from django.views import generic
from .models import BlogPost


# Core from https://djangocentral.com/building-a-blog-application-with-django/
class BlogPostList(generic.ListView):
    queryset = BlogPost.objects.order_by('-created_on')
    template_name = 'blog/blog.html'


class BlogPostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
