from . import views
from django.urls import path

urlpatterns = [
    path('posts', views.PostList.as_view(), name='posts'),
    path('', views.Main.as_view(), name='home'),

]
