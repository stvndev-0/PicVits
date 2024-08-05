from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, ProfileUpdateForm, ChangePasswordForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def profile_view(request, username=None):
    current_user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'profile_user': current_user})

@login_required
def update_password_view(request):
    if request.method == 'POST':
        password_form = ChangePasswordForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            login(request, request.user)
            return redirect('profile')
    else:
        password_form = ChangePasswordForm(request.user)
    return render(request, 'crud/update_password.html', {'password_form': password_form})

@login_required
def update_profile_view(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST or None, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user)
    return render(request, 'crud/update_profile.html', {'profile_form': profile_form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')