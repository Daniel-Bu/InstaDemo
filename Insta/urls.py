from django.urls import path

from Insta.views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('user_profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('explore', ExploreView.as_view(), name='explore'),
]