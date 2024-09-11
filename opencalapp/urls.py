from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('footer/', views.show_footer, name='footer'),
    path('mycalendars/', views.create_calendar,name='mycalendars'),
    path('mycalendars/<calendar_id>', views.delete_calendar, name='delete_calendar'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contact_us, name='contact_us'),
    path('helpcenter/', views.help_center, name='help_center'),
    path('forgotpassword/', views.forgot_password, name='forgot_password'),
    path('account/', views.account, name='account'),
    path('friends/', views.friends, name='friends'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('friends/<user_id>/<is_request>/', views.send_friend_request, name='send_friend_request'),
    path('accept-request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('decline-request/<int:request_id>/', views.decline_friend_request, name='decline_friend_request'),
    path('search_users/', views.search_users, name='search_users'),
]
