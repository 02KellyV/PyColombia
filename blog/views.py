from django.shortcuts import render, redirect
from .models import Post
from django.core.urlresolvers import reverse_lazy
import re


def List(request):
    posts = Post.objects.all()
    return render(request, 'blog/all.html', {'posts': posts})


def Detail(request):
    return


def Creation(request):
    model = Post()
    fields = [
        {'label': 'nombre', 'type': 'text'},
        {'label': 'contenido', 'type': 'textarea'}
    ]
    if request.method == 'POST':
        current_user = request.user
        nombre = request.POST.get('nombre')
        contenido = request.POST.get('contenido')
        model.author_id = current_user.id
        model.title = nombre
        model.text = contenido
        model.publish()
        return redirect('/blog')

    return render(request, 'blog/new.html', {'fields': fields})


def Update(request):
    fields = [
        {'label': 'nombre', 'type': 'text'},
        {'label': 'contenido', 'type': 'textarea'}
    ]
    if request.method == 'POST':
        url = request.build_absolute_uri()
        model = re.sub(r".*[^(/\d)/]", "", url).replace("/", "")
        nombre = request.POST.get('nombre')
        contenido = request.POST.get('contenido')
        model.title = nombre
        model.text = contenido
        model.update()
        return redirect('/blog')
    return render(request, 'blog/edit.html', {'fields': fields})


def Delete(request):
    return
