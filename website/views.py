

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def home(request):
    # bands = models.Band.objects.all()
    return render(request, 'home.html')


def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog')
    else:
        form = UserCreationForm()
    return render(request, 'auth/registration_form.html', {'form': form})


def signIn(request):
    form = AuthenticationForm()
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        if user is not None:
            return redirect('/blog')
        else:
            error = "Los datos del formulario no son validos."

    return render(request, 'auth/login_form.html', {'form': form, 'error': error})
