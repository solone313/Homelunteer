from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.models import User as AuthUser
# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
            profile = Profile.objects.create(user=user,status=request.POST['subject'],Gender=request.POST['gender'],phonenum=request.POST['phone'])
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')