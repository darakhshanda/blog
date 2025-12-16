from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS=((0,"Draft"),(1,"Published"))
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # Title should be unique
    slug = models.SlugField(max_length=200, unique=True) # Slug should be unique
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # Link to User model
    content = models.TextField() # Content of the blog post
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp when the post is created  
    status=models.IntegerField(choices=STATUS, default=0) # Status field to indicate draft or published
    
def __str__(self):
        return self.title
