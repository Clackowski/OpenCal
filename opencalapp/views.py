from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from .forms import RegisterForm, LoginForm, NewCalendarForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Calendar, FriendRequest, FriendList, Account
from django.db.models import Q

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
                return redirect('account')
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
    received_requests = FriendRequest.objects.filter(receiver=request.user, is_active=True)
    friend_list = get_object_or_404(FriendList, user=request.user)
    friends = friend_list.friends.all().order_by('last_name')
    return render(request, 'friends.html', {'user': request.user, 'received_requests': received_requests, 'friends': friends})

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
            new_calendar.owner = request.user;
            new_calendar.save()
            
            form.save_m2m()
            
            contributors = form.cleaned_data.get('contributors')
            for contributor in contributors:
                contributor.calendars.add(new_calendar)
            
            request.user.calendars.add(new_calendar)
            return redirect('mycalendars')
    else:
        form = NewCalendarForm(user=request.user)
    return render(request, 'mycalendars.html', {'form': form})

@login_required
def open_calendar(request, calendar_id):
    calendar = Calendar.objects.get(pk=calendar_id)
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    return render(request, 'opencalendar.html', {'calendar': calendar, 'weekdays': weekdays})

@login_required
def delete_calendar(request, calendar_id):
    calendar = Calendar.objects.get(pk=calendar_id)
    calendar.delete()
    return redirect('mycalendars')

@login_required
def send_friend_request(request, user_id, is_request):
    is_request = (is_request == "true")
    receiver = get_object_or_404(get_user_model(), id=user_id)
    
    if is_request:
        # Friend request sent successfully
        friend_request, created = FriendRequest.objects.get_or_create(sender=request.user, receiver=receiver, is_active=True)
    else:
        # Friend request already exists (unfriend)
        friendList = FriendList.objects.get(user=request.user)
        friendList.friends.remove(receiver)
        
        receiverFriendList = FriendList.objects.get(user=receiver)
        receiverFriendList.friends.remove(request.user)
    
    return redirect('friends')
    

def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user, is_active=True)
    
    if friend_request:
        friend_request.accept()
        friend_request.save()
    
    return redirect('friends')

def decline_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user, is_active=True)
    
    if friend_request:
        friend_request.decline()
        friend_request.save()
    
    return redirect('friends')

def search_users(request):
    query = request.GET.get('query', '').lower()
    if query:
        users = Account.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(username__icontains=query) |
            Q(first_name__icontains=query.split()[0], last_name__icontains=query.split()[-1])
            )
        
        # Get the current user's friends
        current_user = request.user
        friend_list = get_object_or_404(FriendList, user=current_user)
        friends = friend_list.friends.all()
        
        # Prepare user data with friendship status
        user_data = []
        for user in users:
            is_friend = user in friends
            user_data.append({
                'id': user.id,
                'full_name': user.get_full_name(),
                'is_friend': is_friend
            })
    
    else:
        user_data = Account.objects.none()  # Return no users if no query
    
    return render(request, 'partials/user_cards.html', {'users': user_data})

