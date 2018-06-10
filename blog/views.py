from django.shortcuts import render
from .models import Post
from django.core.urlresolvers import reverse_lazy


def List(request):
    return render(request, 'blog/all.html', {'posts': Post.objects.all()})


def Detail(request):
    return


def Creation(request):
    model = Post
    fields = [
        {'label': 'nombre', 'type': 'text'},
        {'label': 'contenido', 'type': 'textarea'}
    ]
    return render(request, 'blog/new.html', {'fields': fields})


def Update(request):
    return


def Delete(request):
    return
