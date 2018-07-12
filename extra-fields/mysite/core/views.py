from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mysite.core.forms import SignUpForm
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from .models import UserDetails

@login_required
def home(request):
    return render(request, 'home.html')


def newslist(request):
    return render(request, 'newslist.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def news(request):
   return render(request, 'news.html')

