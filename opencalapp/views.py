from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.urls import reverse

# Create your views here.
# Request handlers (takes a request and gives a response)

#options are: pull from database, transform data, send email, etc.

#URL Configuration
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if form.get_user().username == 'christopherlackowski':
                return redirect(reverse('admin:index'))
            else:
                return redirect('mycalendars')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        
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

def show_mycalendars(request):
    return render(request, 'mycalendars.html')
