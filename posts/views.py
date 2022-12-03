from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from posts.forms import PostCreateForm, CommentCreateForm
from posts.models import Post,Hashtag,Comment
from users.utils import get_user_from_request

PAGINATION_LIMIT = 4
# Create your views here.

def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)
def posts_view(request):
    if request.method == 'GET':
        hashtag_id = request.GET.get('hashtag_id')
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if hashtag_id:
            posts = Post.objects.filter(hashtags__in=[hashtag_id])
        else:
            posts = Post.objects.all()

        if search_text:
            posts = posts.filter(title__icontains=search_text)

        posts = [{
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'hashtags': post.hashtags.all()
        } for post in posts]

        max_page = round(posts.__len__() / PAGINATION_LIMIT)
        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        data = {
            'posts': posts,
            'user': get_user_from_request(request),
            'hashtag_id': hashtag_id,
            'max_page': range(1, max_page + 1)
        }
        return render(request, 'posts/posts.html', context=data)

def hashtags_view(request, **kwargs):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()
        data = {
            'hashtags': hashtags,
            'user': get_user_from_request(request)
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
            'comments': comments,
            'form':CommentCreateForm,
            'user': get_user_from_request(request)
        }

        return render(request, 'posts/detail.html', context=data)

    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                post_id=kwargs["id"]
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            post = Post.objects.get(id=kwargs["id"])
            comments = Comment.objects.filter(post=post)
            data = {
                'post': post,
                'comments': comments,
                'form': form,
                'user': get_user_from_request(request)

            }
            return render(request,'posts/detail.html',context=data)



def posts_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm,
            'user': get_user_from_request(request)

        }
        return render(request, 'posts/create.html', context=data)

    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            Post.objects.create(
                author_id=1,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),


            )
            return redirect('/posts')
        else:
            data = {
                'form': form,
                'user': get_user_from_request(request)

            }
            return render(request, 'posts/create.html', context=data)