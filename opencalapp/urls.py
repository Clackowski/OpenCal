from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('footer/', views.show_footer, name='footer'),
    path('mycalendars/', views.show_mycalendars, name='mycalendars'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contact_us, name='contact_us'),
    path('helpcenter/', views.help_center, name='help_center'),
    path('forgotpassword/', views.forgot_password, name='forgot_password'),
]
