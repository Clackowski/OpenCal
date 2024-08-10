from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# Request handlers (takes a request and gives a response)

#URL Configuration
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print('here3')
        if form.is_valid():
            print('here2')
            login(request, form.get_user())
            if form.get_user().username == 'christopherlackowski':
                print('here')
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

@login_required
def show_mycalendars(request):
    user = request.user
    print(user.first_name)
    return render(request, 'mycalendars.html', {'user': request.user})

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
    #messages.success(request, ('You were logged out'))
    return redirect('login')