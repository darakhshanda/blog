from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
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
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`mainblog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "mainblog/post_detail.html",
        {"post": post},
    )
