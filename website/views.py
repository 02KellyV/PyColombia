

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
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

    return render(request, 'registration/registration_form.html', {'form': form})

