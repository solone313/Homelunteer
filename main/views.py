from django.shortcuts import render, redirect, get_object_or_404
from .models import Beneficiary, Volunteer
# Create your views here.


def home(request):
    lists = Beneficiary.objects
    return render(request, 'home.html',{'homelist':lists})

def volunteer(request):
    lists = Beneficiary.objects
    return render(request, 'volunteer.html', {'lists':lists})

def gallery(request):
    return render(request, 'gallery.html')

def mypage(request):
    return render(request, 'mypage.html')
    
def about(request):
    return render(request, 'about.html')

def angelhack(request):
    return render(request, 'angelhack.html')