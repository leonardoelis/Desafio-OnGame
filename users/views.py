from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


def register_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = {}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = CustomUserCreationForm()

    context['form'] = form
    return render(request, 'users/registerUser.html', context)


def edit_user(request):
    if request.user.is_anonymous:
        return redirect('login')

    user = User.objects.get(id=request.user.pk)

    context = {}
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserChangeForm(instance=user)

    context['form'] = form
    return render(request, 'users/editUser.html', context)


def change_password(request):
    if request.user.is_anonymous:
        return redirect('login')

    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)

    context['form'] = form
    return render(request, 'users/changePassword.html', context)
