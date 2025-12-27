from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    # published posts only with filtering and ordering
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    # default: <app_label>/<model_name>_list.html
    template_name = "mainblog/index.html"
    paginate_by = 6


# class Main(generic.TemplateView):
#     template_name = "mainblog/index.html"
#     paginate_by = 6
