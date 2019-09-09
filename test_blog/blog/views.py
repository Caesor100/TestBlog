from django.shortcuts import render
from .models import News


def posts_list(request):
    data = {
        'news': News.objects.all(),
        'title': 'Blog home page'
    }
    return render(request, 'blog/index.html', data)
