from django.urls import path

from Insta.views import *

urlpatterns = [
    path('', HelloWorld.as_view(), name='helloworld'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]