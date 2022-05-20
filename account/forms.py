from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    emai = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form__group', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form__group', 'placeholder': 'Password1'}))

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form__group', 'placeholder' : 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form__group', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form__group', 'placeholder': 'Password1'}),
            'password2': forms.PasswordInput(attrs={'class': 'form__group', 'placeholder': 'Password2'}),
        }