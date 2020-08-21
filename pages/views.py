from django.shortcuts import render
from .models import About


def index(request):
    return render(request,'page/index.html')

def about(request):
    abouts = About.objects.all()

    context = {
        'abouts' : abouts,
    }
    return render(request,'page/about.html',context=context)
