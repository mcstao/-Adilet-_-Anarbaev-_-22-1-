from django.urls import path
from posts.views import hello,goodby,now_date,posts_view,hashtags_view,detail_view,posts_create_view

urlpatterns = [
    path('posts/', posts_view),
    path('hello/', hello),
    path('goodby/', goodby),
    path('date/', now_date),
    path('hashtags/', hashtags_view),
    path('posts/<int:id>/', detail_view),
    path('posts/create/',posts_create_view)


]
