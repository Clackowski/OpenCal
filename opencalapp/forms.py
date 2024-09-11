# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import EmailInput, TextInput, PasswordInput

from .models import Account, Calendar, FriendList


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'style' : "width: 100%"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password', 'style' : "width: 100%"}))


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "email", 'style' : "width: 100%"}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': "first name", 'style' : "width: 100%"}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': "last name", 'style' : "width: 100%"}))

    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control", 
                'placeholder': "username",
                'style' : "width: 100%",
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'placeholder': "email",
                'style' : "width: 100%",
                }),
            'first_name': TextInput(attrs={
                'class': "form-control", 
                'placeholder': "first name",
                'style' : "width: 100%",
                }),
            'last_name': TextInput(attrs={
                'class': "form-control", 
                'placeholder': "last name",
                'style' : "width: 100%",
                })
        }
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password', 'style': 'width: 100%'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'repeat password', 'style': 'width: 100%'})


class NewCalendarForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Name',
        'style': 'width: 100%'
    }))
    contributors = forms.ModelMultipleChoiceField(queryset=Account.objects.all(), 
                                                  widget=forms.CheckboxSelectMultiple,
                                                  required=False)
    
    class Meta:
        model = Calendar
        fields = ('name', 'contributors',)
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Customize the widget to display full names
        try:
            friends = FriendList.objects.get(user=user).friends.all()
            self.fields['contributors'].widget.choices = [(friend.id, f"{friend.first_name} {friend.last_name}") for friend in friends]
        except FriendList.DoesNotExist:
            pass