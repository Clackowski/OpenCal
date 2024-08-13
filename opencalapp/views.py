from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm, NewCalendarForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import datetime

# Create your views here.
# Request handlers (takes a request and gives a response)

#URL Configuration
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if form.get_user().username == 'christopherlackowski':
                return redirect(reverse('admin:index'))
            else:
                return redirect('mycalendars')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})


def show_footer(request):
    return render(request, 'footer.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contactus.html')

def help_center(request):
    return render(request, 'helpcenter.html')

def forgot_password(request):
    return render(request, 'forgotpassword.html')

@login_required
def account(request):
    return render(request, 'accountdashboard.html')

@login_required
def friends(request):
    return render(request, 'friends.html')

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def create_calendar(request):
    if request.method == 'POST':
        form = NewCalendarForm(request.POST)
        if form.is_valid():
            new_calendar = form.save(commit=False)
            new_calendar.save()
            request.user.calendars.add(new_calendar)
            return redirect('mycalendars')
    else:
        form = NewCalendarForm()
    return render(request, 'mycalendars.html', {'form': form})
    