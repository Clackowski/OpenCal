from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('footer/', views.show_footer, name='footer'),
    path('mycalendars/', views.create_calendar, name='mycalendars'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contact_us, name='contact_us'),
    path('helpcenter/', views.help_center, name='help_center'),
    path('forgotpassword/', views.forgot_password, name='forgot_password'),
    path('account/', views.account, name='account'),
    path('friends/', views.friends, name='friends'),
    path('settings/', views.settings, name='settings'),
    path('profile', views.profile, name='profile'),
]
