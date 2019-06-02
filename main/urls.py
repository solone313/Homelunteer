from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('gallery/', views.gallery, name='gallery'),
    path('mypage/', views.mypage, name='coaches'),
    path('about/', views.about, name='about'),
    path('angelhack/', views.angelhack, name="angelhack"),
]