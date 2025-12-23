from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    # Title should be unique
    title = models.CharField(max_length=200, unique=True)
    # Slug should be unique
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')  # Link to User model
    content = models.TextField()  # Content of the blog post
    # Timestamp when the post is created
    created_on = models.DateTimeField(auto_now_add=True)
    # Status field to indicate draft or published
    status = models.IntegerField(choices=STATUS, default=0)


class User(models.Model):
    post_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="posts")


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author =models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

def __str__(self):
    return f"Post for {self.title}"
