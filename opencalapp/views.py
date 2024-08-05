from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import RegisterForm, LoginForm
from django.urls import reverse

# Create your views here.
# Request handlers (takes a request and gives a response)

#URL Configuration
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
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

def show_mycalendars(request):
    return render(request, 'mycalendars.html')
