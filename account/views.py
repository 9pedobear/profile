from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreateForm, UserLoginForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

# --------------REGISTER
def register(request):
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
        else:
            messages.error(request, 'При регистрации произошла ошибка')
    return render(request, 'login_register.html', {'register_form': form})

# --------------LOGIN
def loginUser(request):
    page = 'page'
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login_register.html', {'login_form':form,
        'page' : page})

# --------------LOGOUT
def logoutUser(request):
    logout(request)
    return redirect('login')



