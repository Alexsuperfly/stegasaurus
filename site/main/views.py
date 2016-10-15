from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import RegisterForm, SignInForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    title = 'About'
    return render(request, 'main/about.html', {'title': title})

def profile(request):
    title = 'Profile'
    return render(request, 'main/profile.html', {'title': title})

def signin(request):
    title = 'Sign In'

    # We need to process the registration form data
    form = SignInForm(request.POST)
    
    # Check if valid
    if form.is_valid():
        # Process and save the data

        # Eventually redirect to user profile
        # Still need to manage users before being able to handle custom profiles
        return HttpResponseRedirect('/profile')

    else:
        form = SignInForm()

    return render(request, 'main/signin.html', {'form': form, 'title': title})


def register(request):
    title = 'Register'

    # We need to process the registration form data
    form = RegisterForm(request.POST)

    # Check if valid
    if form.is_valid():
        # Process the data
        return HttpResponseRedirect('Success')

    else:
        form = RegisterForm()

    return render(request, 'main/register.html', {'form': form, 'title': title})



