from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', pk=user.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'users/profile.html', {'user': user})

@login_required
def edit_profile(request, pk):
    if request.user.pk != pk:
        return redirect('profile', pk=request.user.pk)
    
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.pk)
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def delete_profile(request, pk):
    if request.user.user_type != 'teacher':
        return redirect('lesson_list')
    
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('register')
    return render(request, 'users/delete_profile.html', {'user': user})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lesson_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})