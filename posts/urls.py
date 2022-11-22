from django.urls import path
from posts.views import hello,goodby,now_date,posts_viev,hashtags_viev,detail_view

urlpatterns = [
    path('posts/', posts_viev),
    path('hello/', hello),
    path('goodby/', goodby),
    path('date/', now_date),
    path('hashtags/', hashtags_viev),
    path('posts/<int:id>/', detail_view),
    path('hashtags', hashtags_viev),

]
