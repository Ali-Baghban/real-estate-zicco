from django.shortcuts import render
from django.http import HttpResponse

def BlogView(request):
    return HttpResponse('<h1>Blog Page</h1>')

def BlogPost(request,id):
    return HttpResponse('<h1>Post Number : </h1>'+str(id))
