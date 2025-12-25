from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "mainblog/post_list.html"
    context_object_name = "object_list"
    paginate_by = 20
