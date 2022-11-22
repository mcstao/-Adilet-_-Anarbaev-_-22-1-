from django.shortcuts import render
from django.http import HttpResponse
import datetime

from posts.models import Post,Hashtag,Comment


# Create your views here.

def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)
def posts_viev(request):
    if request.method == 'GET':
        hashtag_id = request.GET.get('hashtag_id')
        if hashtag_id:
            posts = Post.objects.filter(hashtag_id=hashtag_id)
        else:
            posts = Post.objects.all()



        data = {
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=data)

def hashtags_viev(request, **kwargs):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()
        data = {
            'hashtags': hashtags
        }
        return render(request, 'hashtags/hashtag.html', context=data)
def hello(request):
    if request.method == 'GET':
        return HttpResponse('hello')

def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())

def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


def detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        comments = Comment.objects.filter(post=post)

        data = {
            'post': post,
            'comments': comments
        }

        return render(request, 'posts/detail.html', context=data)
