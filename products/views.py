from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def hello(request):
    if request.method == 'GET':
        return HttpResponse('hello')

def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())

def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')