from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from users import forms


def register_view(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.create(request.POST)
            return redirect('login')
    else:
        form = forms.RegisterForm()
        return render(request, 'register.html', {'form': form})


def user_login(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)  # login funksiyasini to'g'ri chaqirish
            return redirect('register')
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')